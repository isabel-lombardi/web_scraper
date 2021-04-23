<h2>Python Web Scraper</h2>

<p><i>The purpose of the project is to extract the data contained in a PDF file given a specific URL. </i></p>

<h3>How to run</h3>
<p>The program can be run, via the <b>main.py</b> file, from the command line specifying the arguments:
<ul>
    <li><b>state</b>, The name of the State for which you want to extract data</li>
    <li><b>output-path</b>, The name of the folder or path to save files to</li>
</ul>


<h3>Structure</h3>
<ul>
    <li><b>main.py</b>, the entry point file of the program, within it is generated the URL based on 
the choice of the state (The availability is visible in the allowed_states dictionary.)</li>
</ul>

<p> In the main folder:</p>
<ul>
    <li><b>pdfscraper.py</b>, Inside it is present the <b>PDFScraper</b> class that deals with the 
    extraction of the desired file through the HTML structure of the given URL<br>
    <ul>
        <li>The <b>get_pdf</b> method searches the HTML structure, extracts the desired file and clears it from the HTML tags.
        Return the desired file link</li>
        <li>The <b>save_pdf</b> method, given the URL that contains the file, takes care of its saving.</li><br>
</ul>

<li><b>file extract_data.py</b>, Inside it is present the class <b>Extractdata</b></li>
<ul>
        <li><b>data_from_pdf</b> method, which takes care of extracting the tabulated data of the PDF and, 
        after a small processing, to save them in CSV format.</li>
</ul>
</ul>