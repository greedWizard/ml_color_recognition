from color_pick import kns_class, train_set, colors_dict

if __name__ == "__main__":  
    print('Please enter RGB color like RED GREEN BLUE.\t')

    while True:
        unparsed_color = input('R G B:\t')
        unparsed_color = unparsed_color.split()
        
        color = []

        for i in unparsed_color:
            color.append(int(i) if int(i) >= 0 and int(i) <= 255 else 0)
        
        vote = kns_class(train_set, color, k=15)

        print(f'Hmmm.....\nI think it\'s more like {colors_dict[vote]}!')

        answer = input('Is that correct? y/n\n')

        if answer == 'y':
            with open('colors.data', 'at') as f:
                new_data = f'\n{color[0]},{color[1]},{color[2]},{vote}'
                f.write(new_data)
            print('Thank you! Let\'s try that again!')