"""
Вие сте създател на популярен сайт за запознанства и искате да улесните вашите потребители да намерят своята половинка.
За целта вие събирате информация за интересите на всеки потребител и се опитвате да намерите партньор с максимално общи интереси.
Имате дадени два списъка които съдържат интересите на Иванчо и Марийка.
Напишете код който показва само общите интереси между двамата.
"""
ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

print('Иван и Мария споделят следните интереси: ', ', '.join(set(ivan).intersection(set(maria))))

