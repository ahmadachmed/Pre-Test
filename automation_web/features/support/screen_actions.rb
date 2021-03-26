def screenshot(name)
    $browser.save_screenshot("ss/#{name}.png")
    attach("ss/#{name}.png","image/png")
end

def maximize_browser()
    $browser.manage.window.maximize
end

def open_url(url)
    $browser.navigate.to url
end