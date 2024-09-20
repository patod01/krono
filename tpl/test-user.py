from playwright.sync_api import Page, expect

userID = '%s'
passwd = '%s'

def login(page: Page) -> None:
     page.goto('https://trabajador.relojcontrol.com/login.zul')
     expect(page).to_have_url('https://trabajador.relojcontrol.com/login.zul')
     expect(page.locator("#empleado_tab")).to_contain_text("Número de documento")
     expect(page.locator("#empleado_tab")).to_contain_text("Contraseña")
     page.get_by_placeholder('Identificación').fill(userID)
     page.get_by_placeholder('Contraseña').fill(passwd)
     page.get_by_placeholder('Contraseña').press('Enter')
     expect(page).to_have_url('https://trabajador.relojcontrol.com/main.zul')

def main(page: Page) -> None:
     expect(page.locator("#breadcrumbs")).to_contain_text("Registrar asistencia")
     expect(page.locator('body')).to_contain_text('Registrar entrada')
     page.get_by_role("button", name="Registrar entrada").click()
     expect(page.locator("body")).to_contain_text("Registrarás asistencia como")
     page.get_by_role("button", name="Cancelar").click()
     page.wait_for_timeout(5000)
     expect(page.locator('body')).to_contain_text('Registrar salida')
     page.get_by_role("button", name="Registrar salida").click()
     expect(page.locator("body")).to_contain_text("Registrarás asistencia como")
     page.get_by_role("button", name="Cancelar").click()

def logout(page: Page) -> None:
     page.locator('.dropdown-toggle').click()
     page.locator('.dropdown-menu li:last-child a').click()
     expect(page.locator('body')).to_contain_text('¿Cerrar Sesión?')
     page.get_by_role('button', name='OK').click()

def test_user(page: Page) -> None:
     login(page)
     main(page)
     logout(page)
