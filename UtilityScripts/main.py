import json

# function to find the nth occurence of a substring in a string


def find_nth(string, substring, n):
    if (n == 1):
        return string.find(substring)
    else:
        return string.find(substring, find_nth(string, substring, n - 1) + 1)

# function to change the dimension of the thumbnail image by modifying the url string from end (&w=60&h=60& -> &w=544&h=544&)


def change_dimension(string, dimension) -> str:
    thmb_url_str = string
    # print("Original Url - ",thmb_url_str)
    reversed = thmb_url_str[::-1]
    # print(reversed)
    indx_of_first_60_fromLast = find_nth(reversed, '&06=h', 1)
    indx_of_second_60_fromLast = find_nth(reversed, '&06=w', 1)
    to_update_dimension = str(
        "w="+str(dimension)+"&h="+str(dimension)+"&")[::-1]
    reversed = reversed[0:indx_of_first_60_fromLast] + \
        to_update_dimension+reversed[indx_of_second_60_fromLast+5:]

    updated_url_str = reversed[::-1]
    # print("\nUpdated URL = "+updated_url_str)
    return updated_url_str


if __name__ == "__main__":

    req_dimensions = [60, 120, 226, 544]
    req_dimensions.sort()
    file = open('icon_size.json', mode='r')
    # read all data (type:string) and convert it to json (dict)
    icon_data_dict = json.loads(file.read())
    file.close()  # closing the file
    current_icon_objects = len(icon_data_dict["main"])

    write_file = open('restructured_icon_urls.json',
                      "w+")  # file opened for writing
    to_write = '{'
    print("\n>> Current items in 'icon_size.json' file : "+str(current_icon_objects))

    for i in range(0, current_icon_objects):
        icon_name = icon_data_dict["main"][i]["icon_name"]
        to_write += '"'+icon_name+'":{"thumbnails":['
        icon_url = icon_data_dict["main"][i]["icon_url_resizable"]

        for dimnsn in req_dimensions:
            string = '{"url":"'
            modified_url = change_dimension(icon_url, dimnsn)
            string += modified_url+'","width":' + \
                str(dimnsn)+',"height":'+str(dimnsn)
            if(dimnsn != req_dimensions[-1]):
                string += '},'
            else:
                string += '}'
            to_write += string

        if(i == current_icon_objects-1):
            to_write += "]}}"
        else:
            to_write += ']},'

    write_file.write(to_write)
    write_file.close()  # closing the file
