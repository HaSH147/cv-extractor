import re
import unicodedata


class TextExtractor:
    def __init__(self):
        pass


    def normalize_text(self, text: str) -> str:
        # Normalise les accents et convertit en minuscules
        text = unicodedata.normalize('NFKD', text)
        text = ''.join(c for c in text if not unicodedata.combining(c))
        text = text.lower()
        return text

    
    

    
    def extract_email(self, text: str) -> str:
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        return match.group(0) if match else "Indefini"


    def extract_phone(self, text: str) -> str:
        match = re.search(r'\+?\d[\d\s.-]{7,}', text)
        return match.group(0) if match else "Indefini"
    
    


    def extract_firstname(self, text: str) -> str:
        # Extract the first name from the first line
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        
        if not lines:
            return "Indefini"
        
        first_line = lines[0]
        match = re.match(r'^([A-Za-zÀ-ÿ\-]+)\s+([A-Za-zÀ-ÿ\-]+)', first_line)
        
        if match:
            firstname = match.group(1)
            return firstname.lower()
        
        return "Indefini"
    

    def extract_lastname(self, text: str) -> str:
        # Extract last name from the first line
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        
        if not lines:
            return "Indefini"
        
        first_line = lines[0]
        match = re.match(r'^([A-Za-zÀ-ÿ\-]+)\s+([A-Za-zÀ-ÿ\-]+(?:\s+[A-Za-zÀ-ÿ\-]+)?)', first_line)
        
        if match:
            # Get everything after the first name as the last name
            lastname = match.group(2)
            return lastname.lower()
        
        return "Indefini"
    






    def extract_education(self, text: str):
        patterns = [
            r'(licence|bachelor|master|ing[ée]nieur)[^,\n\.@]*',
            r'(b\.?s\.?c|b\.?a|m\.?s\.?c|m\.?a|ph\.?d)[^,\n\.@]*',
        ]
    
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(0)

        return "Indefini"



        


            

    
    def clean_text(self, text: str) -> str:
        text = self.normalize_text(text)
    
        # Normalize line breaks 
        text = text.replace('\r\n', '\n').replace('\r', '\n')
    
        # # Normalize spaces 
        text = re.sub(r'[ \t]+', ' ', text)
    
        return text
    
    def extract_all(self, text: str) -> dict:
        cleaned_text = self.clean_text(text)
        
        return {
            "first_name": self.extract_firstname(cleaned_text),
            "last_name": self.extract_lastname(cleaned_text),
            "email": self.extract_email(cleaned_text),
            "phone": self.extract_phone(cleaned_text),
            "degree": self.extract_education(cleaned_text)
        }