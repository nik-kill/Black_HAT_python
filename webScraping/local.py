from bs4 import BeautifulSoup

#home.html is path of html file

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    """
    courses_html_tags = soup.find_all('h5')
    #print(tags)

    for course in courses_html_tags:
        print(course.text)
    
    """

    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a

        print(f'{course_name} costs {course_price}')