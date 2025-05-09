# Importing libraries
import requests
from collections import Counter
from bs4 import BeautifulSoup

# Function that returns the name of the store from the deal and takes a parameter "listing"
def get_store(listing):

    # Selecting the elements for store from both retailers and normal stores
    store_element_retailer = listing.select_one('.topictitle_retailer')
    store_element = listing.select_one('.topictitle')

    # We see if the retailers exist and then returning their name
    if store_element_retailer:
        return store_element_retailer.text.strip()
    
    elif store_element:
        store_text = store_element.text.strip()
        return store_text.split(']')[0][1:].strip() if ']' in store_text else store_text
    
    # In case no store was found, we return N/A for not applicable
    else:
        return "N/A"

# Function for the main menu where user can choose options
def main_menu():

    while True:
        # \n is very important for readability 
        print("\n\n\n***** Web Scraping Adventure *****\n")
        print("1. Display Latest Deals")
        print("2. Analyze Deals by Category")
        print("3. Find Top Stores")
        print("4. Log Deal Information")
        print("5. Exit")

        # Prompting user to enter a choice that will be checked
        choice = input("Enter your choice (1-5): ")

        # Making sure the user inputs a valid digit and calling the appropriate function
        if choice == '1':
            display_latest_deals()
        elif choice == '2':
            analyze_deals_by_category()
        elif choice == '3':
            find_top_stores()
        elif choice == '4':
            log_deal_information()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        # In case the option is anything other than 1,2,3,4,or 5 
        else:
            print("Invalid choice. Please try again.")

# Function for the most recent deals scraped from the website
def display_latest_deals():

    """
    In this function, we try display 
    the most recent deals scraped from the designated website. It's a 
    little challenging as we could have 30+ deals and thus we need to make
    sure everything is formatted neatly. 
    """
    # This is the link of the website we are trying to scrape
    url = "https://forums.redflagdeals.com/"
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # Example: Extracting information from HTML elements
    # Base URL
    base_url = "https://forums.redflagdeals.com/"
    
    # This will help us count the total number of deals and should be printed first before the deals
    total_deals = len(soup.find_all("li", class_="row topic"))

    # Then we print the total number of deals that we found
    print(f"\n\nTotal deals found: {total_deals}\n")

    # This for loop allows us to display every single deal that was found
    for listing in soup.find_all("li", class_="row topic"):
        store = get_store(listing)

        item_element = listing.select_one('.topic_title_link')
        item = item_element.text.strip() if item_element else "N/A"

        # Grabbing the other options: votes, username, timestampt, category, replies, views, URL
        votes_element = listing.select_one('.total_count_selector')
        votes = votes_element.text.strip() if votes_element else "N/A"

        username_element = listing.select_one('.thread_meta_author')
        username = username_element.text.strip() if username_element else "N/A"

        timestamp_element = listing.select_one('.first-post-time')
        timestamp = timestamp_element.text.strip() if timestamp_element else "N/A"

        category_element = listing.select_one('.thread_category a')
        category = category_element.text.strip() if category_element else "N/A"

        replies_element = listing.select_one('.posts')
        replies = replies_element.text.strip() if replies_element else "N/A"
        
        views_element = listing.select_one('.views')
        views = views_element.text.strip() if views_element else "N/A"

        url_element = item_element['href'] if item_element else "N/A"
        url = base_url + url_element

        # Printing all the elements in the correct order
        print("\nStore:", store)
        print("Item:", item)
        print("Votes:", votes)
        print("Username:", username)
        print("Timestamp:", timestamp)
        print("Category:", category)
        print("Replies:", replies)
        print("Views:", views)
        print("URL:", url)

        # For readability, helps us notice that this section ended
        print("-------------------------")


# Function that allows us to analyse deals based on their category
def analyze_deals_by_category():
    """
    This option allows the user to view all the categories and the number of deals they contain.
    It is a great option for users that wish to understand further the different options provided
    in the scapred data. Thus it adds insights. The challenging part is to align the categories
    and the deals in a neat way. 
    """
    # URL of the RedFlagDeals forum hot deals section, the website we are trying to scrape
    url = "https://forums.redflagdeals.com/"
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # Scraping the category details and counting the deals based on their category
    categories = {}

    for listing in soup.find_all("li", class_="row topic"):
        category_element = listing.select_one('.thread_category a')
        category = category_element.text.strip() if category_element else "N/A"
        categories[category] = categories.get(category, 0) + 1

    # Printing the number of deals based on their category
    print("\nDeals by Category:\n")

    maximum_categories = max(len(category) for category in categories)
    number_of_categories = len(categories)

    for i, (category, count) in enumerate(categories.items(), 1):

        if i == number_of_categories:
            print(f"{category.rjust(maximum_categories)}: {count} deals")
            print("------------------------------------------------------------")

        else:
            print(f"{category.rjust(maximum_categories)}: {count} deals")


# Function that will allow user to find the top n stores
def find_top_stores():
    """
    This function prompts the user to enter a number of top stores theu wish to see displayed. 
    Each top storer will be shown along the number of their deals.
    """
    # URL of the RedFlagDeals forum hot deals section, the website we are trying to scrape
    url = "https://forums.redflagdeals.com/"
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # Scraping the category details and counting the deals based on their category
    stores = Counter()

    for listing in soup.find_all("li", class_="row topic"):
        store = get_store(listing)
        stores[store] += 1

    # Prompting the user for the number of top stores to be displayed
    while True:

        try:
            num_of_topStores = int(input("Enter the number of top stores to display: "))
            break
        # If the number is not valid
        except ValueError:
            print("Please enter a valid number.")

    # Showing the n number of top stores
    print("\nTop Stores:\n")

    # We can choose the number of n stores we wish to display to user
    maximum_stores = 30  
    num_stores = len(stores)

    for i, (store, count) in enumerate(stores.most_common(num_of_topStores), 1):
        if i == num_stores:
            print(f"{store.ljust(maximum_stores)}: {count} deals")
            print("-----------------------------------------------------------------")
        else:
            print(f"{store.ljust(maximum_stores)}: {count} deals")
            


# Function to get the categories based of the deal listings
def get_categories(soup):

    categories = set()
    
    for listing in soup.find_all("li", class_="row topic"):
        category_element = listing.select_one('.thread_category a')

        if category_element:
            categories.add(category_element.text.strip())

    return list(categories)

# Function to display all available categories
def log_deal_information():

    # URL of the RedFlagDeals forum hot deals section, the website we are trying to scrape
    url = "https://forums.redflagdeals.com/"
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    categories = get_categories(soup)

    # Making sure I add the \n for readability
    print("\n\nList of Categories:\n")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:

        try:
            category_choice = int(input("Enter the number corresponding to the category: "))
            if 1 <= category_choice <= len(categories):
                selected_category = categories[category_choice - 1]

                with open("log.txt", "a") as log_file:
                    for listing in soup.find_all("li", class_="row topic"):
                        category_element = listing.select_one('.thread_category a')
                        category = category_element.text.strip() if category_element else "N/A"
                        if category == selected_category:
                            item_element = listing.select_one('.topic_title_link')
                            url_element = item_element['href'] if item_element else "N/A"
                            url = url_element
                            log_file.write(f"{url}\n")

                print("All the links have been logged successfully.")

                break  
            
            # In case the number is not legal
            else:
                print("Invalid category number.")

            # In case the input is not integer
        except ValueError:

            print("Invalid input. Please enter a number.")

# Main function 
def main():
   
    url = "https://forums.redflagdeals.com/"
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # Example: Extracting information from HTML elements
    # Base URL
    base_url = "https://forums.redflagdeals.com/"
    
    for listing in soup.find_all("li", class_="row topic"):
        store = get_store(listing)

        item_element = listing.select_one('.topic_title_link')
        item = item_element.text.strip() if item_element else "N/A"
        
     
        url_element = item_element['href'] if item_element else "N/A"
        url = base_url + url_element
        

    #Calling my main menu to display options and prompt user
    main_menu()

if __name__ == "__main__":
    main()
