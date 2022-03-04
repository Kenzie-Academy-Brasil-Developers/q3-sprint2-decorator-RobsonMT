def test_route_login_exists(app_post_routes):
    assert app_post_routes.match(
        "/login"
    ), 'Verifique se existe uma rota "/login apta para POST"'


def test_route_register_exists(app_post_routes):
    assert app_post_routes.match(
        "/register"
    ), 'Verifique se existe uma rota "/register apta para POST"'
