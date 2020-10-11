import webbrowser
from reportlab.pdfgen import canvas
def getTotal(list):
  total=0
  for data in list:
    total=total+data[4]
  return total

def getTotalTax(list):
  totalTax=0
  for data in list:
    totalTax=totalTax+data[5]
  return totalTax

def getTotalDis(list):
  totalDis=0
  for data in list:
    totalDis=totalDis+data[3]
  return totalDis

def rightalingn(pdf,string,left,right,ycoordinate):
  length=len(string)
  totalLength=(right-left)/7
  print(totalLength)
  spaces=int(totalLength-length)
  print(spaces)
  pdf.drawString(right,ycoordinate," "*spaces)
  left=left+(7*spaces)
  pdf.drawString(left,ycoordinate,string)

def header(header,pdf):
  pdf.setTitle(header.date+"Invoice")
  # logo="logo.jpeg"
  # pdf.drawInlineImage(logo,190,253)

  pdf.line(30,815,350,815)
  pdf.setFont("Courier-Bold",20)
  pdf.drawString(30,800,"Shop Name")
  pdf.setFont("Courier-Bold",11)
  pdf.drawString(30,785,"Address Line1,")
  pdf.drawString(30,770,"Address Line2,")
  pdf.drawString(30,755,"Pincode. Phone: Contact Number")

  pdf.line(30,753,350,753)

  pdf.drawString(30,735,"Invoice Number: "+ str(int(header.InvoiceNumber)))
  pdf.drawString(30,720,"Customer Name: "+ str(header.CustomerName))
  pdf.drawString(30,705,"Contact Number: "+ str(header.CustomerContact))
  pdf.drawString(30,690,"Date: "+ str(header.date))
  



def middle(pdf):
  pdf.line(30,677,550,677)
  
  pdf.drawString(30,668,"Sr.No.")
  pdf.drawString(75,668,"Product Name")
  pdf.drawString(200,668,"Quantity")
  pdf.drawString(260,668,"Rate")

  pdf.drawString(400,668,"Total")

  
  pdf.line(30,662,550,662)
  pdf.line(73,677,73,150)
  pdf.line(198,677,198,150)
  pdf.line(258,677,258,150)
  pdf.line(398,677,398,150)
  pdf.line(30,150,550,150)

def additem(product,pdf,ycoordinate):
  while(len(product.name)>18):
    pdf.drawString(75,ycoordinate,product.name[:18]+"-")
    product.name=product.name[18:]
    ycoordinate=ycoordinate-15
  
  pdf.drawString(75,ycoordinate,product.name)
  pdf.drawString(200,ycoordinate,str(product.quantity))
  rightalingn(pdf,"%.2f" %product.rate,260,316,ycoordinate)
  print(product.rate)

  rightalingn(pdf,"%.2f" %product.total,400,488,ycoordinate)

  return (ycoordinate-15)

def footer(pdf,list):
  pdf.drawString(30, 120, "Gross Total:")
  rightalingn(pdf, "%.2f" % getTotal(list) + " INR", 400, 488, 120)
  pdf.drawString(30,135,"tax:")
  rightalingn(pdf, "+" + "%.2f" % getTotalTax(list) + " INR", 393, 488, 135)
  total=getTotalTax(list)+getTotal(list)


  pdf.line(30,100,550,100)
  pdf.drawString(30,90,"Grand Total: ")
  rightalingn(pdf,"%.2f" %total+" INR",400,488,90)
  pdf.drawString(400,30,"Authorized Signatory")


def About():
  pdf=canvas.Canvas("C:\\InvoiceGenerator\\about.pdf")
  pdf.setFont("Courier-Bold",20)
  pdf.drawString(40,700,"Paurush Kumar Gupta")
  pdf.setFont("Courier-Bold",15)
  pdf.drawString(40,650,"Student, ")
  pdf.drawString(40,630,"Computer Science & Engineering,")
  pdf.drawString(40,610,"Noida Institute of Engineering & Technology,")
  pdf.drawString(40,590,"Greater Noida, 201310.")
  pdf.drawString(40,550,"Contact: gpaurush39@gmail.com")
  pdf.save()
  webbrowser.open("C:\\InvoiceGenerator\\about.pdf")
