# services/report_generator.py

# The '..' is removed from the import below to make it an absolute import.
import models

def generate_html_report(complaint: models.Complaint) -> str:
    """
    Generates a simplified HTML report for a given complaint, styled to look
    like a MedWatch 3500A form.
    """
    # Using an f-string to build the HTML structure.
    # Inline CSS is used for styling to keep it self-contained.
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MedWatch 3500A Report - Complaint ID: {complaint.id}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; color: #333; }}
            .container {{ border: 2px solid #000; padding: 20px; }}
            .header {{ text-align: center; margin-bottom: 20px; }}
            .header h1 {{ margin: 0; font-size: 24px; }}
            .header p {{ margin: 5px 0; }}
            .section {{ border: 1px solid #000; margin-bottom: 20px; }}
            .section-title {{ background-color: #000; color: #fff; padding: 5px; font-weight: bold; }}
            .section-content {{ padding: 10px; }}
            .field {{ margin-bottom: 10px; }}
            .field-label {{ font-weight: bold; }}
            .field-value {{ border: 1px solid #ccc; padding: 5px; background-color: #f9f9f9; min-height: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <p>DEPARTMENT OF HEALTH AND HUMAN SERVICES</p>
                <h1>MedWatch</h1>
                <p>The FDA Safety Information and Adverse Event Reporting Program</p>
            </div>

            <div class="section">
                <div class="section-title">A. PATIENT INFORMATION</div>
                <div class="section-content">
                    <div class="field">
                        <div class="field-label">Complaint ID:</div>
                        <div class="field-value">{complaint.id}</div>
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-title">B. ADVERSE EVENT OR PRODUCT PROBLEM</div>
                <div class="section-content">
                    <div class="field">
                        <div class="field-label">1. Adverse Event and/or Product Problem:</div>
                        <div class="field-value">{complaint.defect}</div>
                    </div>
                     <div class="field">
                        <div class="field-label">2. Outcomes Attributed to Adverse Event:</div>
                        <div class="field-value" style="color: red; font-weight: bold;">{complaint.severity.upper()}</div>
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-title">C. SUSPECT PRODUCT(S)</div>
                <div class="section-content">
                    <div class="field">
                        <div class="field-label">1. Name, Strength, Manufacturer:</div>
                        <div class="field-value">{complaint.device_name}</div>
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-title">D. NARRATIVE</div>
                <div class="section-content">
                    <div class="field">
                        <div class="field-label">Describe Event, Problem, or Product Use/Medication Error:</div>
                        <div class="field-value" style="white-space: pre-wrap;">{complaint.raw_transcript}</div>
                    </div>
                </div>
            </div>

        </div>
    </body>
    </html>
    """
    return html_content
