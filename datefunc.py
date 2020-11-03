def date_item(ymd, length):
    
    entered_length = length  
    while length == entered_length:

        enter_ymd = input(f'Please enter {ymd}:')
        try:
            int(enter_ymd)
        except ValueError:
            print('Please enter four digits only.')
        
        if len(enter_ymd) != length:
            print('Year must be 4 digits.')
        else:
            add_ymd = enter_ymd
            print(add_ymd)
            return add_ymd

new_year = date_item('Year', 4)
