import csv
import urllib.parse

html = ""
with open('paper_inf.csv', 'r') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split(',')
        if len(parts) >= 3:
            title = parts[0]
            if len(parts) > 3 and "CVPR" in parts[1]:
                # Handline "CVPR 2021,1,5"
                venue = parts[1].strip() + " " + parts[2].strip()
                img_name = parts[3].strip() + ".png"
            else:
                venue = parts[1].strip()
                img_name = parts[2].strip() + ".png"
            
            link = "https://scholar.google.com/scholar?q=" + urllib.parse.quote_plus(title)
            
            html += f"""    <tr>
        <td style="padding:20px;width:25%;vertical-align:middle">
            <img src="paper_imgs/{img_name}" alt="{title}" width="160" style="border-style: none">
        </td>
        <td width="75%" valign="middle">
            <a href="{link}">
            <papertitle>{title}</papertitle>
            </a>
            <br>
            <em>{venue}</em>
            <br>
            <p></p>
        </td>
    </tr>
"""
print(html)
