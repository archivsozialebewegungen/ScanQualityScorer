# ScanQualityScorer
Creates a score how fit a graphical text scan is for OCR

## Installation

Make sure you have tesseract version 4.1 or higher.

Clone the project:

    git clone https://github.com/archivsozialebewegungen/ScanQualityScorer.git
    cd ScanQualityScorer

Create and activate a virtual environment:

    python3 -m venv --copies venv
    source venv/bin/activate
    
Install requirements:

    pip3 install -r requirements.txt

## Execution

Just run <code>ScanQualityScorer.sh</code> in the <code>bin</code> directory with the graphical image file as parameter:

	ScanQualityScorer.sh my_text_file.jpg
