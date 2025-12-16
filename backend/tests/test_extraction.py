from services.extractor import TextExtractor


def test_extract_email():
    text = "Contactez noous sur cette adresse at test.email@gmail.com for more info."
    extractor = TextExtractor()

    result = extractor.extract_email(text)

    assert result == "test.email@gmail.com"


def test_extract_phone():
    text = "numéro de téléphone est : +331234567890"
    extractor = TextExtractor()

    result = extractor.extract_phone(text)

    assert result == "+331234567890"


def test_extract_degree():
    extractor = TextExtractor()
    text = "Ingénieure en Informatique et mathématiques appliquées."

    result = extractor.extract_education(text)

    assert "ingenieur" in result
