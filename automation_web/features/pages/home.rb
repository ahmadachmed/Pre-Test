$search_field = 'v-omnisearch__input'


def input_home_search_field(keywords)
    $browser.find_element(:id,$search_field).send_keys(keywords)
end

def submit_home_search_field()
    $browser.find_element(:id,$search_field).send_keys:enter
end

def validate_title(title)
    current_title = $browser.title
    puts "page title is #{current_title}"
    expect(current_title).to include(title)   
end