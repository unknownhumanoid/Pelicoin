import flet as ft


async def main(page: ft.Page) -> None:
    import micropip

    await micropip.install("sqlite3")

    page.title = "Pelicoin Banking"
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
        "/accounts/education": views.getEducationView,
        "/accounts/retirement": views.getRetirementView,
        "/admin": views.getAdminView,
    }

    async def changeRoute(e: ft.RouteChangeEvent):
        e.page.views.clear()
        newView = await routeToView.get(e.route)(page)
        e.page.views.append(newView)
        await page.update_async()

    page.on_route_change = changeRoute

    await page.go_async("/login")


# app = flet_fastapi.app(main, assets_dir="/Users/lucaslevine/Documents/ISP 2/assets")
app = ft.app(main, assets_dir="/Users/lucaslevine/Documents/ISP 2/assets")
