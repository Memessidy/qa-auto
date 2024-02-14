AMAZON_PRODUCT_XPATH = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span'
# TODO Необхідний аттрибут зміг знайти тільки по такому складному XPATH, так як 1 символ там постійно змінюється
custom_xpath = ("//*[starts-with(@aria-label, '1') or starts-with(@aria-label, '2')"
                " or starts-with(@aria-label, '3') or starts-with(@aria-label, '4')"
                " or starts-with(@aria-label, '5') or starts-with(@aria-label, '6') "
                "or starts-with(@aria-label, '7') or starts-with(@aria-label, '8') "
                "or starts-with(@aria-label, '9')]/descendant-or-self::*[contains(@aria-label, "
                "'unread conversations')]")