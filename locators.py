from selenium.webdriver.common.by import By


class StellarburgerSearch:

    Button_login_page = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка для перехода на страницу входа в ЛК
    Button_reg = (By.XPATH, "//a[text()='Зарегистрироваться']") #Кнопка для перехода на страницу регистрации
    Button_reg_new_user = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка регистрации нового пользователя

    Head_personal_accoount = (By.XPATH, ".//h2[text()='Вход']") #Заголовок страницы входа
    Head_reg_page = (By.TAG_NAME, "h2") #Заголовок страницы Регистрации

    Input_reg_name = (By.NAME, "name") #Ввод имени нового пользователя
    Input_reg_email = (By.XPATH, "//fieldset[2]//input[@name='name']") #Ввод email нового пользователя
    Input_reg_password = (By.NAME, "Пароль") #Ввод пароля нового пользователя

    False_reg_password = (By.XPATH, "//fieldset[3]/div/p[text()='Некорректный пароль']") #Ошибка некорректный пароль

    Input_name = (By.NAME, "name") #Ввод email на странице входа в лк
    Input_password = (By.NAME, "Пароль") #Ввод пароля на странице входа в лк

    Button_logout = (By.XPATH, "//button[text()='Войти']") #Кнопка входа в лк
    Head_main = (By.XPATH, "//section[1]/h1[text()='Соберите бургер']") #Заголовок основной страницы
    Button_personal_account = (By.XPATH, "//p[text()='Личный Кабинет']") #Кнопка входа в лк
    Button_logout_form_reg = (By.XPATH, "//a[text()='Войти']") #Кнопка входа в форме регистрации
    Button_password_recovery = (By.XPATH, "//a[text()='Восстановить пароль']") #Кнопка восстановить пароль
    Head_password_recovery = (By.XPATH, "//h2[text()='Восстановление пароля']") #Заголовок страници восстановдения пароля
    Button_password_recovery_login = (By.XPATH, "//a[text()='Войти']") #Кнопка войти на странце восстановления пароля

    Info_personal_account = (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']") #Инфо в разделе личного кабинета
    Button_constructor = (By.XPATH, "//li[1]/a/p[text()='Конструктор']") #Кнопка перехода в конструктор и ЛК
    Button_exit_personal_account = (By.XPATH, "//li[3]/button[text()='Выход']")  # Кнопка выхода из лк


    Button_chapter_buns = (By.XPATH, "//span[text()='Булки']") #Раздел с булками
    Button_chapter_sauces = (By.XPATH, "//span[text()='Соусы']") #Раздел с соусами
    Button_chapter_fillings = (By.XPATH, "//span[text()='Начинки']") #Раздел с начинками


    Input_name_buns =  (By.XPATH, "//a[2]/p[text()='Краторная булка N-200i']")
    Input_name_sauses =  (By.XPATH, "//a[3]/p[text()='Соус традиционный галактический']")
    Input_name_fillings =  (By.XPATH, "//a[2]/p[text()='Говяжий метеорит (отбивная)']")





