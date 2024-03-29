import flet as ft
import sys

local = not sys.platform == "emscripten"
appView = ft.AppView.FLET_APP


async def main(page: ft.Page) -> None:
    if not local:
        global appView
        appView = ft.AppView.WEB_BROWSER

    if local:
        page.window_width, page.window_height = 400, 850

    page.title = "Pelicoin Banking"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.fonts = {
        "Kayak Light": "fonts/Kayak Sans Light.otf",
        "Kayak Regular": "fonts/Kayak Sans Regular.otf",
        "Kayak Bold": "fonts/Kayak Sans Bold.otf",
    }

    import views

    routeToView = {
        "/login": views.getLogInView,
        "/signup": views.getSignUpView,
        "/accounts": views.getAccountsView,
        "/accounts/current": views.getCurrentView,
        "/accounts/current/transfer": views.getTransferViewGenerator("current"),
        "/accounts/education": views.getEducationView,
        "/accounts/education/transfer": views.getTransferViewGenerator("education"),
        "/accounts/retirement": views.getRetirementView,
        "/accounts/retirement/transfer": views.getTransferViewGenerator("retirement"),
        "/accounts/transactions": views.getTransactionsView,
        "/admin": views.getAdminView,
    }

    async def changeRoute(e: ft.RouteChangeEvent):
        e.page.views.clear()
        newView = await routeToView.get(e.route)(page)
        e.page.views.append(newView)
        await page.update_async()

    page.on_route_change = changeRoute

    await page.go_async("/login")


app = ft.app(main)
