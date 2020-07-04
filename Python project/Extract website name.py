url = input("Website URL:")
first_index = url.index(".")
second_index = url.index(".", first_index+1)
website_name = url[first_index+1:second_index]
print(website_name)