Given("I am on the Bukalapak page") do
    maximize_browser()
    open_url("https://bukalapak.com")
    sleep(2)
end

When("I search for {string}") do |keywords|
    input_home_search_field(keywords)
    sleep(2)
    submit_home_search_field()
end

Then("the page title should have {string}") do |keywords|
    validate_title(keywords)
    screenshot("#{keywords}")
end