import os
import pickle
import pandas as pd
from django.conf import settings
from django.shortcuts import render

MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor', 'model', 'bangalore_pipeline.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def home(request):
    prediction = None
    error = None

    if request.method == 'POST':
        try:
            location = request.POST.get('location')
            sqft = request.POST.get('total_sqft')
            bath = request.POST.get('bath')
            bhk = request.POST.get('bhk')

            # Validation
            if not all([location, sqft, bath, bhk]):
                raise ValueError("All fields are required")

            sqft = float(sqft)
            bath = int(bath)
            bhk = int(bhk)

            if sqft <= 0 or bath <= 0 or bhk <= 0:
                raise ValueError("Values must be positive")

            input_df = pd.DataFrame([{
                'location': location,
                'total_sqft': sqft,
                'bath': bath,
                'bhk': bhk
            }])

            pred = model.predict(input_df)[0]
            prediction = round(pred, 2)

        except Exception as e:
            error = str(e)

    return render(request, 'index.html', {
    'prediction': prediction,
    'error': error,
    'locations': sorted([
         #'Whitefield', 'Indira Nagar', 'Electronic City', 'other'
        '1st Block Jayanagar', '1st Phase JP Nagar', '2nd Phase Judicial Layout', '2nd Stage Nagarbhavi', '5th Block Hbr Layout', '5th Phase JP Nagar', '6th Phase JP Nagar', '7th Phase JP Nagar', '8th Phase JP Nagar', '9th Phase JP Nagar', 'AECS Layout', 'Abbigere', 'Akshaya Nagar', 'Ambalipura', 'Ambedkar Nagar', 'Amruthahalli', 'Anandapura', 'Ananth Nagar', 'Anekal', 'Anjanapura', 'Ardendale', 'Arekere', 'Attibele', 'BEML Layout', 'BTM 2nd Stage', 'BTM Layout', 'Babusapalaya', 'Badavala Nagar', 'Balagere', 'Banashankari', 'Banashankari Stage II', 'Banashankari Stage III', 'Banashankari Stage V', 'Banashankari Stage VI', 'Banaswadi', 'Banjara Layout', 'Bannerghatta', 'Bannerghatta Road', 'Basavangudi', 'Basaveshwara Nagar', 'Battarahalli', 'Begur', 'Begur Road', 'Bellandur', 'Benson Town', 'Bharathi Nagar', 'Bhoganhalli', 'Billekahalli', 'Binny Pete', 'Bisuvanahalli', 'Bommanahalli', 'Bommasandra', 'Bommasandra Industrial Area', 'Bommenahalli', 'Brookefield', 'Budigere', 'CV Raman Nagar', 'Chamrajpet', 'Chandapura', 'Channasandra', 'Chikka Tirupathi', 'Chikkabanavar', 'Chikkalasandra', 'Choodasandra', 'Cooke Town', 'Cox Town', 'Cunningham Road', 'Dasanapura', 'Dasarahalli', 'Devanahalli', 'Devarachikkanahalli', 'Dodda Nekkundi', 'Doddaballapur', 'Doddakallasandra', 'Doddathoguru', 'Domlur', 'Dommasandra', 'EPIP Zone', 'Electronic City', 'Electronic City Phase II', 'Electronics City Phase 1', 'Frazer Town', 'GM Palaya', 'Garudachar Palya', 'Giri Nagar', 'Gollarapalya Hosahalli', 'Gottigere', 'Green Glen Layout', 'Gubbalala', 'Gunjur', 'HAL 2nd Stage', 'HBR Layout', 'HRBR Layout', 'HSR Layout', 'Haralur Road', 'Harlur', 'Hebbal', 'Hebbal Kempapura', 'Hegde Nagar', 'Hennur', 'Hennur Road', 'Hoodi', 'Horamavu Agara', 'Horamavu Banaswadi', 'Hormavu', 'Hosa Road', 'Hosakerehalli', 'Hoskote', 'Hosur Road', 'Hulimavu', 'ISRO Layout', 'ITPL', 'Iblur Village', 'Indira Nagar', 'JP Nagar', 'Jakkur', 'Jalahalli', 'Jalahalli East', 'Jigani', 'Judicial Layout', 'KR Puram', 'Kadubeesanahalli', 'Kadugodi', 'Kaggadasapura', 'Kaggalipura', 'Kaikondrahalli', 'Kalena Agrahara', 'Kalyan nagar', 'Kambipura', 'Kammanahalli', 'Kammasandra', 'Kanakapura', 'Kanakpura Road', 'Kannamangala', 'Karuna Nagar', 'Kasavanhalli', 'Kasturi Nagar', 'Kathriguppe', 'Kaval Byrasandra', 'Kenchenahalli', 'Kengeri', 'Kengeri Satellite Town', 'Kereguddadahalli', 'Kodichikkanahalli', 'Kodigehaali', 'Kodigehalli', 'Kodihalli', 'Kogilu', 'Konanakunte', 'Koramangala', 'Kothannur', 'Kothanur', 'Kudlu', 'Kudlu Gate', 'Kumaraswami Layout', 'Kundalahalli', 'LB Shastri Nagar', 'Laggere', 'Lakshminarayana Pura', 'Lingadheeranahalli', 'Magadi Road', 'Mahadevpura', 'Mahalakshmi Layout', 'Mallasandra', 'Malleshpalya', 'Malleshwaram', 'Marathahalli', 'Margondanahalli', 'Marsur', 'Mico Layout', 'Munnekollal', 'Murugeshpalya', 'Mysore Road', 'NGR Layout', 'NRI Layout', 'Nagarbhavi', 'Nagasandra', 'Nagavara', 'Nagavarapalya', 'Narayanapura', 'Neeladri Nagar', 'Nehru Nagar', 'OMBR Layout', 'Old Airport Road', 'Old Madras Road', 'Padmanabhanagar', 'Pai Layout', 'Panathur', 'Parappana Agrahara', 'Pattandur Agrahara', 'Poorna Pragna Layout', 'Prithvi Layout', 'R.T. Nagar', 'Rachenahalli', 'Raja Rajeshwari Nagar', 'Rajaji Nagar', 'Rajiv Nagar', 'Ramagondanahalli', 'Ramamurthy Nagar', 'Rayasandra', 'Sahakara Nagar', 'Sanjay nagar', 'Sarakki Nagar', 'Sarjapur', 'Sarjapur  Road', 'Sarjapura - Attibele Road', 'Sector 2 HSR Layout', 'Sector 7 HSR Layout', 'Seegehalli', 'Shampura', 'Shivaji Nagar', 'Singasandra', 'Somasundara Palya', 'Sompura', 'Sonnenahalli', 'Subramanyapura', 'Sultan Palaya', 'TC Palaya', 'Talaghattapura', 'Thanisandra', 'Thigalarapalya', 'Thubarahalli', 'Thyagaraja Nagar', 'Tindlu', 'Tumkur Road', 'Ulsoor', 'Uttarahalli', 'Varthur', 'Varthur Road', 'Vasanthapura', 'Vidyaranyapura', 'Vijayanagar', 'Vishveshwarya Layout', 'Vishwapriya Layout', 'Vittasandra', 'Whitefield', 'Yelachenahalli', 'Yelahanka', 'Yelahanka New Town', 'Yelenahalli', 'Yeshwanthpur', 'other'
        # paste full list here (or load dynamically later)
        ])
    })