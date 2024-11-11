from django import forms

# List of available Google Places API search types
SEARCH_TYPES = [
    ('accounting', 'Accounting'),('airport', 'Airport'),('amusement_park', 'Amusement Park'),('aquarium', 'Aquarium'),('art_gallery', 'Art Gallery'),('atm', 'ATM'),
    ('bakery', 'Bakery'),('bank', 'Bank'),('bar', 'Bar'),('beauty_salon', 'Beauty Salon'),('bicycle_store', 'Bicycle Store'),('book_store', 'Book Store'),
    ('bowling_alley', 'Bowling Alley'),('bus_station', 'Bus Station'),
    ('cafe', 'Cafe'),('campground', 'Campground'),('car_dealer', 'Car Dealer'),('car_rental', 'Car Rental'),('car_repair', 'Car Repair'),('car_wash', 'Car Wash'),
    ('casino', 'Casino'),('cemetery', 'Cemetery'),('church', 'Church'),('city_hall', 'City Hall'),('clothing_store', 'Clothing Store'),
    ('convenience_store', 'Convenience Store'),('courthouse', 'Courthouse'),
    ('dentist', 'Dentist'),('department_store', 'Department Store'),('doctor', 'Doctor'),
    ('electrician', 'Electrician'),('electronics_store', 'Electronics Store'),('embassy', 'Embassy'),
    ('fire_station', 'Fire Station'),('florist', 'Florist'),('funeral_home', 'Funeral Home'),('furniture_store', 'Furniture Store'),
    ('gas_station', 'Gas Station'),('gym', 'Gym'),
    ('hair_care', 'Hair Care'),('hardware_store', 'Hardware Store'),('hindu_temple', 'Hindu Temple'),('home_goods_store', 'Home Goods Store'),('hospital', 'Hospital'),
    ('insurance_agency', 'Insurance Agency'),
    ('jewelry_store', 'Jewelry Store'),
    ('laundry', 'Laundry'),('lawyer', 'Lawyer'),('library', 'Library'),('light_rail_station', 'Light Rail Station'),('liquor_store', 'Liquor Store'),
    ('local_government_office', 'Local Government Office'),('locksmith', 'Locksmith'),('lodging', 'Lodging'),
    ('meal_delivery', 'Meal Delivery'),('meal_takeaway', 'Meal Takeaway'),('mosque', 'Mosque'),('movie_rental', 'Movie Rental'),('movie_theater', 'Movie Theater'),
    ('moving_company', 'Moving Company'),('museum', 'Museum'),
    ('night_club', 'Night Club'),
    ('painter', 'Painter'),('park', 'Park'),('parking', 'Parking'),('pet_store', 'Pet Store'),('pharmacy', 'Pharmacy'),('physiotherapist', 'Physiotherapist'),
    ('plumber', 'Plumber'),('police', 'Police'),('post_office', 'Post Office'),('primary_school', 'Primary School'),
    ('real_estate_agency', 'Real Estate Agency'),('restaurant', 'Restaurant'),('roofing_contractor', 'Roofing Contractor'),('rv_park', 'RV Park'),
    ('school', 'School'),('secondary_school', 'Secondary School'),('shoe_store', 'Shoe Store'),('shopping_mall', 'Shopping Mall'),('spa', 'Spa'),
    ('stadium', 'Stadium'),('storage', 'Storage'),('store', 'Store'),('subway_station', 'Subway Station'),('supermarket', 'Supermarket'),('synagogue', 'Synagogue'),
    ('taxi_stand', 'Taxi Stand'),('tourist_attraction', 'Tourist Attraction'),('train_station', 'Train Station'),('transit_station', 'Transit Station'),
    ('travel_agency', 'Travel Agency'),
    ('university', 'University'),
    ('veterinary_care', 'Veterinary Care'),
    ('zoo', 'Zoo'),
]

# List of headers to include in the Excel file
HEADERS = [
    ('Place Name', 'Place Name'),
    ('Vicinity', 'Vicinity'),
    ('Formatted Address', 'Formatted Address'),
    ('Maps URL', 'Maps URL'),
    ('Rating', 'Rating'),
    ('User Ratings Total', 'User Ratings Total'),
    ('Types', 'Types'),
    ('Business Status', 'Business Status'),
    ('Price Level', 'Price Level'),
    ('Phone Number', 'Phone Number'),
    ('Website', 'Website'),
    ('Opening Hours', 'Opening Hours'),
    ('Open Now', 'Open Now')
]

# Form definition
class PlaceSearchForm(forms.Form):
    address = forms.CharField(
        label="Address", 
        max_length=255, 
        widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': 'Location Address', 'id': 'address', 'style': 'height: 55px;'})
    )
    longitude = forms.DecimalField(widget=forms.HiddenInput(attrs={'id': 'longitude'}))
    latitude = forms.DecimalField(widget=forms.HiddenInput(attrs={'id': 'latitude'}))
    radius = forms.IntegerField(label="Radius (meters)", min_value=1000, max_value=50000, widget=forms.HiddenInput(attrs={'id': 'radius'}))
    search_types = forms.MultipleChoiceField(label="Search Types", choices=SEARCH_TYPES, widget=forms.CheckboxSelectMultiple)
    headers = forms.MultipleChoiceField(label="Excel Headers", choices=HEADERS, widget=forms.CheckboxSelectMultiple)
