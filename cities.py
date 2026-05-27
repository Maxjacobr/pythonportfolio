#Max Rubenstein
#Images

import webbrowser

#Functions

#Main
cities_to_visit = ["https://res.cloudinary.com/aenetworks/image/upload/c_fill,w_1200,h_630,g_auto/dpr_auto/f_auto/q_auto:eco/v1/gettyimages-1390815938", "https://images.musement.com/cover/0002/42/view-on-manhattan-at-night-new-york-city_header-141511.jpeg?w=1200&h=630&q=95&fit=crop", "https://www.dubai.it/en/wp-content/uploads/sites/142/dubai-marina-hd.jpg",  "https://media.timeout.com/images/106253396/750/422/image.jpg"]


def make_recomendation():
    beach = input("Do you care about beach access (y or n): ")
    if beach == "y":
        shopping = input("Are you planning on going on a fancy shopping spree (y or n): ")
        if shopping == "y":
            print("Based on your answers, you should visit Dubai!")
            webbrowser.open(cities_to_visit[2])
        elif shopping == "n":
            print("Based on your answers, you should visit Sydney!")
            webbrowser.open(cities_to_visit[3])
    elif beach == "n":
        international = input("Would you like to stay in the US (y or n): ")
        if international == "y":
            print("Based on your answers, you should visit New York City!")
            webbrowser.open(cities_to_visit[1])
        if international == "n":
            print("Based on your answers, you should visit Tokyo!")
            webbrowser.open(cities_to_visit[0])
make_recomendation()


#Sources of information

#Picture of Tokyo
#History.com
#URL: https://res.cloudinary.com/aenetworks/image/upload/c_fill,w_1200,h_630,g_auto/dpr_auto/f_auto/q_auto:eco/v1/gettyimages-1390815938
#Author name: Barbara Maranzani
#Article Title: 6 Things You Should Know About Tokyo

#Picture of NY
#Website: https://www.musement.com/us/new-york/
#URL: https://images.musement.com/cover/0002/42/view-on-manhattan-at-night-new-york-city_header-141511.jpeg?w=1200&h=630&q=95&fit=crop

#Picture of Dubai
#Website: https://www.dubai.it/en/things-to-do-dubai/dubai-marina/
#URL: https://www.dubai.it/en/wp-content/uploads/sites/142/dubai-marina-hd.jpg
#Article name: Dubai Marina

#Picture of Sydney
#Website: https://www.timeout.com/australia/news/vivid-sydney-2025-the-essential-guide-for-travellers-to-australias-biggest-festival-of-light-031625
#URL: https://media.timeout.com/images/106253396/750/422/image.jpg
#Author name: Melissa Woodley
#Date: March 16th 2025
#Article title: Vivid Sydney 2025: the essential guide for travellers to Australia's biggest festival of light
