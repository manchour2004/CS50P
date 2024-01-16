from fpdf import FPDF


def main():
    string = input("Name: ")

    pdf = FPDF()
    pdf.add_page(format=(210, 297))
    pdf.image("shirtificate.png", w=180, x=10, y=70)

    pdf.set_font("Times", "B", size=36)

    pdf.set_text_color(0,0,0)
    pdf.cell(180, 10, f"CS50 Shirtificate", align="C")
    pdf.ln(10)

    pdf.set_text_color(255,255,255)
    pdf.cell(180, 230, f"{string} took CS50", align="C")
    pdf.ln(100)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()