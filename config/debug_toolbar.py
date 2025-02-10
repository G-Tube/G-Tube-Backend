def setup_debug_toolbar(
    debug: bool,
    installed_apps: list[str],
    middleware: list[str],
    internal_ips: list,
):
    if not debug:
        return
    installed_apps.append("debug_toolbar")
    middleware.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    internal_ips.extend(
        (
            "127.0.0.1",
            "localhost",
        )
    )
