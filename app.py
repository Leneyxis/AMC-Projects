from flask import Flask, render_template

app = Flask(__name__)

# List of video details (title and Google Drive embed URL)
videos = [
    {
        "title": "Product Tracking Blockchain",
        "url": "https://drive.google.com/file/d/10st5q19q9CSjb3iifHcWgfymileCnKRU/preview"
    },
    {
        "title": "Bike Lock and Unlocking",
        "url": "https://drive.google.com/file/d/1u7pFIC4MheUIfVdhuo_H_Mud7L02NAeI/preview"
    },
    {
        "title": "Coddy",
        "url": "https://drive.google.com/file/d/1_mnkW5EbvYeKr3OsA2DPRv6vkVHCWhAz/preview"
    },
    {
        "title": "Dark Web Monitoring",
        "url": "https://drive.google.com/file/d/1JBWde7rWuk1ZvRjoNOdg_E4kb_R3Vfep/preview"
    },
    {
        "title": "Fishfeeder using IOT",
        "url": "https://drive.google.com/file/d/1miV_SwUWettL3sBSLw_PIAwBWCRWgMvI/preview"
    },
    {
        "title": "Protection of Crops from animals",
        "url": "https://drive.google.com/file/d/1J8BxHs0KZq_7_rhVosr_mBN_qMPxKShE/preview"
    },
    {
        "title": "Railway Management using IOT",
        "url": "https://drive.google.com/file/d/1eD-_cgb3jJoDfnEbzdN8_a5aVEvu4M0s/preview"
    },
    {
        "title": "RAM Dump Collector",
        "url":"https://drive.google.com/file/d/1QM-JPEwQ_vE06dM5CW6A1gL_siosrcwQ/preview"
    },
    {
        "title":"Real time Vehicle Tracking",
        "url":"https://drive.google.com/file/d/13WqsQrKlIaqy2Dslb2sk5Er09g9NTOAj/preview"
    },
    {
        "title":"Plant Disease Detection App",
        "url":"https://drive.google.com/file/d/1U5MfS_FdkOVWmsAZpwj7_QVWJ6cwl5H9/preview"
    },
    {
        "title":"Bike Pooling App",
        "url":"https://drive.google.com/file/d/17StDlntNNuB2Y4eCzwxVHY8PBqQxWn8D/preview"
    },
    {
        "title":"Sign Language App",
        "url":"https://drive.google.com/file/d/1Z2O6OrO6_DkInZWeEsAhxGJV8axWucIy/preview"
    },
    {
        "title":"Cyberbullying Detection App",
        "url":"https://drive.google.com/file/d/1EBHr0l1CgblvEMxWUGaKTEXiJnMuHDGR/preview"
    },
    {
        "title":"Personality Prediction",
        "url":"https://drive.google.com/file/d/1znl-4IPWvX0v8P5Nkr1Y54dLKVJvrjxJ/preview"
    },
    {
        "title":"Prediction of Cardiac Abnormalities",
        "url":"https://drive.google.com/file/d/1aXG7uM5fFX8nC7Lg553pBkE15S-_vE-e/preview"
    },
    {
        "title":"Deepfake Detector",
        "url":"https://drive.google.com/file/d/1aKI3itFMqmj_6EZfQolsCjVWYD1yp3Qr/preview"
    },
    {
        "title":"My Safetipin Device for Women",
        "url":"https://drive.google.com/file/d/1Cbl01mL8XI44QDr3X3-6Txmaj93TY4XR/preview"
    },
    {
        "title":"AR Indoor Mapping",
        "url":"https://drive.google.com/file/d/19m-7xEeR9Bmao9HbxD2jI0un6WEyy443/preview"
    },
    {
        "title":"Derman",
        "url":"https://drive.google.com/file/d/18d_sIiZYUMmxvHl6p80gtl1HtKcQ_GYs/preview"
    },
    {
        "title":"TAYD",
        "url":"https://drive.google.com/file/d/1_8uPDWImJMr9qJMXkeKycYaetCIsr63N/preview"
    },
    {
        "title":"AI Powered gym posture",
        "url":"https://drive.google.com/file/d/1HWQU8fhVJQ3ZHUTUyLM0J7iiSXgomYUt/preview"
    },
    {
        "title":"Biometric ATM System",
        "url":"https://drive.google.com/file/d/15-fl5dsGQs2E4thXnNOMjkmKSyPBtWII/preview"
    },
    {
        "title":"Morse Code",
        "url":"https://drive.google.com/file/d/1ojzWZ00E5-Lm2ROekNO0L-fEpIue60zJ/preview"
    },
    {
        "title":"Smart Metering System",
        "url":"https://drive.google.com/file/d/18bZ2RnLdIzTCuiEDciJiBnEtObHk_W7U/preview"
    },
    {
        "title":"Safefuard Homesense",
        "url":"https://drive.google.com/file/d/1PGJho9c2dJPJgwX_kLm4lVk-DvrQbGVT/preview"
    },
    {
        "title":"3D Protein Prediction System",
        "url":"https://drive.google.com/file/d/1RfZf9fR0fDNmHKIcFAETJuWH7F1XyxN3/preview"
    },
    {
        "title":"Advanced Surveillance System for Parking",
        "url":"https://drive.google.com/file/d/1CVVOxTB5DwcXBTsUzOG6kxJTVLz4jxYY/preview"
    },
    {
        "title":"Detection of Brute Force on IOT Networks",
        "url":"https://drive.google.com/file/d/1jBQ-Q_QPk0LVxMAY0uawN1UNgnmqeQg9/preview"
    },
    {
        "title":"Strengthening Cybersecurity",
        "url":"https://drive.google.com/file/d/1L_t89xDJaONiFZlNpG6TdibeWJZQFeK6/preview"
    },
    {
        "title":"Smart Diary",
        "url":"https://drive.google.com/file/d/1NROCORoayx6AflQVuWq3iFePtY5xt47T/preview"
    },
    {
        "title":"Real Estate Transaction",
        "url":"https://drive.google.com/file/d/1AZzqLmO2C46xMulF02RRL28cXvJfaM_X/preview"
    },
    {
        "title":"EHR using blockchain",
        "url":"https://drive.google.com/file/d/1x-ilKRwpI_Hglvol8o2iexSWIERkEfUF/preview"
    },
    {
        "title":"AI Rotoscoping Project",
        "url":"https://drive.google.com/file/d/1BxRohENwfoTkexjWrdzqYb2N_0sreWIc/preview"
    },
    {
        "title":"Online Legal Connections System",
        "url":"https://drive.google.com/file/d/10AQOTcmJ5U-0hVq0ebzyfwBAKiBBPFNN/preview"
    },
    {
        "title":"Diabetes Prediction",
        "url":"https://drive.google.com/file/d/1N-V-4saA_dnfS-E5ubbCpDbWkpS6s_FT/preview"
    },
    {
        "title":"Spot Cloud",
        "url":"https://drive.google.com/file/d/1ZHRkbuirwMuTN60qj5GTL-9gQBZWxWba/preview"
    },
    {
        "title":"Currency Detection App",
        "url":"https://drive.google.com/file/d/1pPFkyvFDy2w1Xazk40gpd0ZCQZUL5BIW/preview"
    },
    {
        "title":"Phishing Link Detection",
        "url":"https://drive.google.com/file/d/1q-qGuU52I31OCC7jvecRzrMmwveBpAzb/preview"
    },
    {
        "title":"Automatic TimeTable Log",
        "url":"https://drive.google.com/file/d/19TD3ej_ecnM2A2d9-kn4jf_T1K3LOBiR/preview"
    },
    {
        "title":"Mineral AI",
        "url":"https://drive.google.com/file/d/1ZZWHfSFOzHLVLL3RzjqTlAmzhxNDin81/preview"
    },
    {
        "title":"Multicloud Guard",
        "url":"https://drive.google.com/file/d/1aK6VMTrk34hlBc_iH9XCqgez3i72tHny/preview"
    }
]

@app.route('/')
def index():
    return render_template('index.html', videos=videos)
    
if __name__ == "__main__":
    app.run(debug=True)
