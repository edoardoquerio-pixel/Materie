"""Rebuild presentation with images properly integrated into slide layouts."""
from pathlib import Path
import subprocess, sys

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
    from pptx.oxml.ns import qn
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-pptx"])
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
    from pptx.oxml.ns import qn

IMG = Path(r"C:\Users\edoardo.querio\OneDrive - ITS ICT Piemonte\Desktop\Materie\_img_extracted")
DST = Path(r"C:\Users\edoardo.querio\OneDrive - ITS ICT Piemonte\Desktop\Materie\01_Inglese_Tecnico\00_Note\Cloud_Computing_Presentation_UPDATED.pptx")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Colors
NAVY = RGBColor(0x1B, 0x3A, 0x5C)
BLUE = RGBColor(0x2E, 0x86, 0xC1)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LGRAY = RGBColor(0xF5, 0xF6, 0xFA)
DGRAY = RGBColor(0x2C, 0x3E, 0x50)
MGRAY = RGBColor(0x7F, 0x8C, 0x9A)
RED = RGBColor(0xE7, 0x4C, 0x3C)
GREEN = RGBColor(0x27, 0xAE, 0x60)
ORANGE = RGBColor(0xF3, 0x9C, 0x12)
LBLUE = RGBColor(0xD6, 0xEA, 0xF8)

def solid_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def rect(slide, l, t, w, h, color, border=False):
    from pptx.enum.shapes import MSO_SHAPE
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    s.fill.solid()
    s.fill.fore_color.rgb = color
    if not border:
        s.line.fill.background()
    return s

def txtbox(slide, l, t, w, h, text, sz=18, color=DGRAY, bold=False, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(sz)
    p.font.color.rgb = color
    p.font.bold = bold
    p.alignment = align
    return tf

def bullets(slide, l, t, w, h, items, sz=16, color=DGRAY, spacing=Pt(4)):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = item
        p.font.size = Pt(sz)
        p.font.color.rgb = color
        p.space_after = spacing
    return tf

def section_header(slide, num, title, subtitle=""):
    solid_bg(slide, NAVY)
    rect(slide, Inches(0), Inches(3.3), Inches(13.333), Inches(0.05), BLUE)
    txtbox(slide, Inches(1), Inches(1.3), Inches(11), Inches(0.5),
           f"Section {num}", sz=18, color=BLUE, bold=True)
    txtbox(slide, Inches(1), Inches(1.9), Inches(11), Inches(1.2),
           title, sz=40, color=WHITE, bold=True)
    if subtitle:
        txtbox(slide, Inches(1), Inches(3.7), Inches(11), Inches(0.8),
               subtitle, sz=18, color=RGBColor(0xBB,0xCC,0xDD))

def content_slide(slide, title, items):
    solid_bg(slide, WHITE)
    rect(slide, Inches(0), Inches(0), Inches(13.333), Inches(1.0), NAVY)
    txtbox(slide, Inches(0.8), Inches(0.15), Inches(11), Inches(0.7),
           title, sz=26, color=WHITE, bold=True)
    rect(slide, Inches(0.8), Inches(1.0), Inches(3), Inches(0.04), BLUE)
    bullets(slide, Inches(0.8), Inches(1.4), Inches(11.5), Inches(5.5),
            items, sz=17, color=DGRAY)

def text_left_img_right(slide, title, items, img_file, img_w=None, img_h=None):
    """Text on left half, image on right half."""
    solid_bg(slide, WHITE)
    rect(slide, Inches(0), Inches(0), Inches(13.333), Inches(1.0), NAVY)
    txtbox(slide, Inches(0.8), Inches(0.15), Inches(11), Inches(0.7),
           title, sz=26, color=WHITE, bold=True)
    rect(slide, Inches(0.8), Inches(1.0), Inches(3), Inches(0.04), BLUE)
    bullets(slide, Inches(0.5), Inches(1.3), Inches(6.0), Inches(5.5),
            items, sz=16, color=DGRAY)
    img_path = IMG / img_file
    if img_path.exists():
        if img_w and img_h:
            slide.shapes.add_picture(str(img_path), Inches(6.8), Inches(1.3), img_w, img_h)
        else:
            slide.shapes.add_picture(str(img_path), Inches(6.8), Inches(1.3), Inches(5.8), Inches(5.5))

def text_right_img_left(slide, title, items, img_file, img_w=None, img_h=None):
    """Image on left half, text on right half."""
    solid_bg(slide, WHITE)
    rect(slide, Inches(0), Inches(0), Inches(13.333), Inches(1.0), NAVY)
    txtbox(slide, Inches(0.8), Inches(0.15), Inches(11), Inches(0.7),
           title, sz=26, color=WHITE, bold=True)
    rect(slide, Inches(0.8), Inches(1.0), Inches(3), Inches(0.04), BLUE)
    img_path = IMG / img_file
    if img_path.exists():
        if img_w and img_h:
            slide.shapes.add_picture(str(img_path), Inches(0.5), Inches(1.3), img_w, img_h)
        else:
            slide.shapes.add_picture(str(img_path), Inches(0.5), Inches(1.3), Inches(6.0), Inches(5.5))
    bullets(slide, Inches(6.8), Inches(1.3), Inches(6.0), Inches(5.5),
            items, sz=16, color=DGRAY)

def img_below_text(slide, title, items, img_file, img_w=None, img_h=None):
    """Text on top half, image centered below."""
    solid_bg(slide, WHITE)
    rect(slide, Inches(0), Inches(0), Inches(13.333), Inches(1.0), NAVY)
    txtbox(slide, Inches(0.8), Inches(0.15), Inches(11), Inches(0.7),
           title, sz=26, color=WHITE, bold=True)
    rect(slide, Inches(0.8), Inches(1.0), Inches(3), Inches(0.04), BLUE)
    bullets(slide, Inches(0.8), Inches(1.3), Inches(11.5), Inches(2.0),
            items, sz=15, color=DGRAY)
    img_path = IMG / img_file
    if img_path.exists():
        if img_w and img_h:
            slide.shapes.add_picture(str(img_path), Inches(6.6 - img_w/2), Inches(3.3), img_w, img_h)
        else:
            slide.shapes.add_picture(str(img_path), Inches(1.5), Inches(3.3), Inches(10), Inches(3.8))

def two_col_slide(slide, title, left_title, left_items, right_title, right_items):
    solid_bg(slide, WHITE)
    rect(slide, Inches(0), Inches(0), Inches(13.333), Inches(1.0), NAVY)
    txtbox(slide, Inches(0.8), Inches(0.15), Inches(11), Inches(0.7),
           title, sz=26, color=WHITE, bold=True)
    rect(slide, Inches(0.8), Inches(1.0), Inches(3), Inches(0.04), BLUE)
    rect(slide, Inches(0.5), Inches(1.4), Inches(5.8), Inches(0.5), BLUE)
    txtbox(slide, Inches(0.7), Inches(1.45), Inches(5.4), Inches(0.4),
           left_title, sz=18, color=WHITE, bold=True)
    bullets(slide, Inches(0.5), Inches(2.1), Inches(5.8), Inches(5.0),
            left_items, sz=15, color=DGRAY)
    rect(slide, Inches(6.8), Inches(1.4), Inches(5.8), Inches(0.5), RED)
    txtbox(slide, Inches(7.0), Inches(1.45), Inches(5.4), Inches(0.4),
           right_title, sz=18, color=WHITE, bold=True)
    bullets(slide, Inches(6.8), Inches(2.1), Inches(5.8), Inches(5.0),
            right_items, sz=15, color=DGRAY)


# =======================================================
# SLIDE 1: TITLE
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
solid_bg(s, NAVY)
rect(s, Inches(0), Inches(3.2), Inches(13.333), Inches(0.05), BLUE)
txtbox(s, Inches(1), Inches(0.8), Inches(11), Inches(1.2),
       "Cloud Computing Fundamentals", sz=48, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
txtbox(s, Inches(1), Inches(2.1), Inches(11), Inches(0.8),
       "A Technical Presentation", sz=28, color=BLUE, align=PP_ALIGN.CENTER)
txtbox(s, Inches(1), Inches(3.7), Inches(11), Inches(1.5),
       "Evolution  •  Service Models  •  Deployment Models\nServerless  •  Edge Computing  •  Cloud-Native",
       sz=18, color=RGBColor(0xBB,0xCC,0xDD), align=PP_ALIGN.CENTER)
txtbox(s, Inches(1), Inches(5.8), Inches(11), Inches(0.5),
       "Cloud Specialist Course — ITS ICT Piemonte",
       sz=16, color=RGBColor(0x88,0x99,0xAA), align=PP_ALIGN.CENTER)

# =======================================================
# SLIDE 2: AGENDA
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
content_slide(s, "Agenda", [
    "1.  Introduction — What is Cloud Computing?",
    "2.  Evolution: From Data Centers to the Cloud",
    "3.  Service Models: IaaS, PaaS, SaaS",
    "4.  Deployment Models: Public, Private, Hybrid, Multi-Cloud",
    "5.  Advantages & Disadvantages",
    "6.  Edge Computing vs Cloud Computing",
    "7.  Serverless Computing",
    "8.  Cloud-Native Applications",
    "9.  Real-World Case Studies",
    "10. Summary & Conclusions"
])

# =======================================================
# SLIDE 3: SECTION 1 HEADER
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, 1, "What is Cloud Computing?",
               "Definition, characteristics, and how it works")

# =======================================================
# SLIDE 4: INTRO - What is Cloud (image1)
# image1: 743x625 - medium diagram
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_left_img_right(s, "What is Cloud Computing?", [
    "Delivery of computing services over the internet",
    "Servers, storage, databases, networking, analytics, software",
    "",
    "Key characteristics:",
    "  •  On-demand self-service — provision via API/click",
    "  •  Broad network access — from any device",
    "  •  Resource pooling — economies of scale",
    "  •  Rapid elasticity — scale with demand",
    "  •  Measured service — pay-as-you-go",
    "",
    "Instead of owning hardware,",
    "you rent what you need and pay for what you use."
], "image1.png", Inches(5.8), Inches(5.0))

# =======================================================
# SLIDE 5: Evolution (image3 small square)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_right_img_left(s, "Evolution: Data Centers → Cloud", [
    "Traditional Data Centers:",
    "  •  Physical servers, high CapEx, weeks to provision",
    "  •  Fixed capacity — over-provision or crash",
    "  •  On-premise maintenance, limited DR",
    "",
    "Cloud Computing:",
    "  •  Virtualized resources, OpEx, minutes to provision",
    "  •  Elastic — scales with demand automatically",
    "  •  Provider handles infra, geo-redundant DR",
], "image3.png", Inches(5.5), Inches(5.0))

# =======================================================
# SLIDE 6: Timeline (image13 - large diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_left_img_right(s, "Key Milestones", [
    "2006: Amazon launches AWS (S3 + EC2) — public cloud born",
    "2008: Google App Engine — first PaaS",
    "2010: Microsoft Azure commercially available",
    "2014: AWS Lambda — serverless computing",
    "2015: Kubernetes 1.0 — container orchestration standard",
    "2020s: Multi-cloud, hybrid, edge become mainstream",
    "",
    "Infrastructure shifted from capital asset to programmable service.",
    "Infrastructure as Code (IaC) via Terraform, CloudFormation."
], "image13.png", Inches(5.8), Inches(5.5))

# =======================================================
# SLIDE 7: Evolution comparison (image2 - table/diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
img_below_text(s, "Traditional vs Cloud — Comparison", [
    "Traditional: buy servers, wait weeks, fixed capacity, manual ops, limited DR",
    "Cloud:     rent resources, instant provisioning, elastic, automated, geo-redundant"
], "image2.png", Inches(10.5), Inches(3.5))

# =======================================================
# SLIDE 8: SECTION 2 HEADER
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, 2, "Cloud Service Models", "IaaS  •  PaaS  •  SaaS")

# =======================================================
# SLIDE 9: IaaS (image14 - landscape diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_right_img_left(s, "IaaS — Infrastructure as a Service", [
    "Provider offers: VMs, storage, network, load balancers",
    "You manage: OS, middleware, runtime, apps, data",
    "",
    "Maximum control, maximum responsibility",
    "",
    "Use cases:",
    "  •  Migrating existing workloads without changes",
    "  •  Full control over the software stack",
    "",
    "Examples: AWS EC2, GCE, Azure VMs"
], "image14.png", Inches(5.8), Inches(5.5))

# =======================================================
# SLIDE 10: PaaS (image12 - landscape diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_left_img_right(s, "PaaS — Platform as a Service", [
    "Provider manages: OS, runtime, middleware, scaling, patching",
    "You manage: code and data only",
    "",
    "Focus on development, not infrastructure",
    "",
    "Use cases:",
    "  •  Web apps and APIs",
    "  •  Rapid prototyping and MVPs",
    "",
    "Examples: Google App Engine, Heroku, Azure App Services"
], "image12.png", Inches(5.8), Inches(5.5))

# =======================================================
# SLIDE 11: SaaS (image4 - landscape diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_right_img_left(s, "SaaS — Software as a Service", [
    "Provider manages everything: hardware, platform, app, data",
    "You just use it — open a browser and log in",
    "",
    "Zero installation, zero maintenance",
    "",
    "Examples:",
    "  •  Gmail, Microsoft 365, Salesforce",
    "  •  Dropbox, Slack, Zoom",
    "",
    "The most common cloud model for end users"
], "image4.png", Inches(5.8), Inches(5.5))

# =======================================================
# SLIDE 12: Service Models Comparison (image6 - labeled diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_left_img_right(s, "Service Models Comparison", [
    "IaaS (You manage more):",
    "  Apps | Data | Runtime | Middleware | OS",
    "  Provider: VMs | Storage | Network",
    "",
    "PaaS (Balance):",
    "  Apps | Data",
    "  Provider: Runtime | Middleware | OS | Infra",
    "",
    "SaaS (Provider manages everything):",
    "  Everything managed by provider",
    "  You just use the application"
], "image6.png", Inches(5.8), Inches(5.5))

# =======================================================
# SLIDE 13: SECTION 3 HEADER
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, 3, "Cloud Deployment Models",
               "Public  •  Private  •  Hybrid  •  Multi-Cloud")

# =======================================================
# SLIDE 14: Deployment Models (4 quadrants)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
solid_bg(s, WHITE)
rect(s, Inches(0), Inches(0), Inches(13.333), Inches(1.0), NAVY)
txtbox(s, Inches(0.8), Inches(0.15), Inches(11), Inches(0.7),
       "Cloud Deployment Models", sz=26, color=WHITE, bold=True)
rect(s, Inches(0.8), Inches(1.0), Inches(3), Inches(0.04), BLUE)

models = [
    ("Public Cloud", "Shared infrastructure\nAWS, Azure, GCP\nNo CapEx, elastic\nLess control", Inches(0.5), Inches(1.4), Inches(5.8), Inches(2.7), BLUE),
    ("Private Cloud", "Dedicated infra\nVMware, OpenStack\nFull control, secure\nHigh cost", Inches(6.8), Inches(1.4), Inches(5.8), Inches(2.7), RED),
    ("Hybrid Cloud", "Mix on-prem + cloud\nFlexibility, compliance\nOperational complexity", Inches(0.5), Inches(4.4), Inches(5.8), Inches(2.7), GREEN),
    ("Multi-Cloud", "Multiple providers\nNo vendor lock-in\nMulti-platform expertise", Inches(6.8), Inches(4.4), Inches(5.8), Inches(2.7), ORANGE),
]

for name, desc, l, t, w, h, color in models:
    rect(s, l, t, w, h, color)
    txtbox(s, l + Inches(0.3), t + Inches(0.15), w - Inches(0.6), Inches(0.5),
           name, sz=20, color=WHITE, bold=True)
    txtbox(s, l + Inches(0.3), t + Inches(0.7), w - Inches(0.6), h - Inches(1.0),
           desc, sz=14, color=WHITE)

# =======================================================
# SLIDE 15: SECTION 4 HEADER
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, 4, "Advantages & Disadvantages",
               "A balanced look at cloud computing pros and cons")

# =======================================================
# SLIDE 16: Pros & Cons
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
two_col_slide(s, "Cloud Computing: Pros & Cons",
    "Advantages",
    ["No upfront CapEx — pay-as-you-go OpEx",
     "Elasticity — scale instantly with demand",
     "Faster time-to-market — infra in minutes",
     "Global reach — deploy in regions worldwide",
     "Enterprise-grade security",
     "Built-in disaster recovery",
     "Automatic updates and patching"],
    "Disadvantages",
    ["Unpredictable costs without monitoring",
     "Internet dependency",
     "Vendor lock-in — expensive migration",
     "Limited control during provider outages",
     "Compliance constraints (healthcare, finance)",
     "Data sovereignty regulations",
     "Latency for real-time applications"])

# =======================================================
# SLIDE 17: SECTION 5 HEADER
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, 5, "Edge Computing vs Cloud Computing",
               "Centralized vs distributed processing")

# =======================================================
# SLIDE 18: Edge vs Cloud (image16)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_left_img_right(s, "Edge vs Cloud Computing", [
    "Cloud Computing:",
    "  •  Centralized data centers",
    "  •  High computing power",
    "  •  Higher latency (50-500ms)",
    "  •  Analytics, ML training, storage",
    "",
    "Edge Computing:",
    "  •  Processing near data source",
    "  •  Ultra-low latency (<10ms)",
    "  •  Real-time decisions, IoT",
    "  •  Autonomous vehicles, smart cities"
], "image16.png", Inches(5.8), Inches(5.5))

# =======================================================
# SLIDE 19: Edge use cases (image5 - architecture diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
img_below_text(s, "Edge Computing — Use Cases", [
    "Autonomous vehicles, industrial IoT, smart cities, healthcare, retail",
    "Complementary: Edge handles real-time, Cloud handles complex analytics",
    "Gartner: 75% of enterprise data processed at edge by 2028"
], "image5.png", Inches(10.5), Inches(3.8))

# =======================================================
# SLIDE 20: SECTION 6 HEADER
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, 6, "Serverless Computing",
               "Run code without managing servers")

# =======================================================
# SLIDE 21: Serverless (image9 - diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_right_img_left(s, "Serverless Computing", [
    "Write functions — cloud handles everything else",
    "No server provisioning, no OS management",
    "",
    "How it works:",
    "  •  Upload function code",
    "  •  Connect to event (HTTP, upload, DB change)",
    "  •  Cloud runs only when triggered",
    "  •  Pay per execution (millisecond billing)",
    "",
    "Providers: AWS Lambda, Azure Functions, GCP Functions",
    "Ideal for: intermittent workloads, webhooks, mobile backends"
], "image9.png", Inches(5.8), Inches(5.0))

# =======================================================
# SLIDE 22: SECTION 7 HEADER
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, 7, "Cloud-Native Applications",
               "Designed for the cloud from day one")

# =======================================================
# SLIDE 23: Cloud-Native pillars (image7 - architecture)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
text_left_img_right(s, "Cloud-Native Applications", [
    "Not just \"running on cloud\" — designed FOR the cloud",
    "",
    "Four pillars:",
    "1. Microservices — small, independent services",
    "2. Containers — Docker + Kubernetes",
    "3. DevOps & CI/CD — automated deployments",
    "4. Resilience & Observability",
    "     (retries, circuit breakers, tracing)",
    "",
    "Examples: Netflix, Spotify, Uber",
    "Scale and speed impossible without cloud-native design"
], "image7.png", Inches(5.8), Inches(5.0))

# =======================================================
# SLIDE 24: Cloud-Native stack (image8 - detailed diagram)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
img_below_text(s, "Cloud-Native Architecture", [
    "Microservices packaged in containers, orchestrated by Kubernetes, deployed via CI/CD pipelines",
    "Observability: centralized logging, metrics, distributed tracing"
], "image8.png", Inches(8.5), Inches(5.0))

# =======================================================
# SLIDE 25: SECTION 8 HEADER
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
section_header(s, 8, "Real-World Case Studies",
               "How industry leaders use cloud computing")

# =======================================================
# SLIDE 26: Case studies (image15 + image10)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
solid_bg(s, WHITE)
rect(s, Inches(0), Inches(0), Inches(13.333), Inches(1.0), NAVY)
txtbox(s, Inches(0.8), Inches(0.15), Inches(11), Inches(0.7),
       "Real-World Case Studies", sz=26, color=WHITE, bold=True)
rect(s, Inches(0.8), Inches(1.0), Inches(3), Inches(0.04), BLUE)

cases = [
    ("Netflix", "Migrated from data centers to AWS\n200M+ subscribers, microservices,\nautoscaling, global CDN"),
    ("Spotify", "Built on Google Cloud\nBig data analytics, ML for\npersonalized recommendations"),
    ("Uber", "Cloud-native from day one\nMicroservices + Kubernetes\n70+ countries, millions of rides"),
    ("Healthcare", "Secure medical record storage\nTelemedicine, remote diagnostics\nAI-powered imaging analysis"),
]

for i, (name, desc) in enumerate(cases):
    col = i % 2
    row = i // 2
    l = Inches(0.5 + col * 6.3)
    t = Inches(1.4 + row * 2.8)
    rect(s, l, t, Inches(5.8), Inches(2.4), LGRAY)
    rect(s, l, t, Inches(0.06), Inches(2.4), BLUE if i % 2 == 0 else RED)
    txtbox(s, l + Inches(0.3), t + Inches(0.15), Inches(5.2), Inches(0.5),
           name, sz=20, color=NAVY, bold=True)
    txtbox(s, l + Inches(0.3), t + Inches(0.7), Inches(5.2), Inches(1.5),
           desc, sz=14, color=DGRAY)

# =======================================================
# SLIDE 27: Case study images (image15 - Netflix case)
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
solid_bg(s, WHITE)
rect(s, Inches(0), Inches(0), Inches(13.333), Inches(1.0), NAVY)
txtbox(s, Inches(0.8), Inches(0.15), Inches(11), Inches(0.7),
       "Cloud Architecture Examples", sz=26, color=WHITE, bold=True)
rect(s, Inches(0.8), Inches(1.0), Inches(3), Inches(0.04), BLUE)
# image15 on left
img15 = IMG / "image15.png"
if img15.exists():
    s.shapes.add_picture(str(img15), Inches(0.3), Inches(1.3), Inches(6.0), Inches(5.5))
# image10 on right
img10 = IMG / "image10.png"
if img10.exists():
    s.shapes.add_picture(str(img10), Inches(6.8), Inches(1.3), Inches(6.0), Inches(5.5))

# =======================================================
# SLIDE 28: Summary
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
content_slide(s, "Summary", [
    "Cloud computing = on-demand access to computing resources over the internet",
    "",
    "Three service models: IaaS (infrastructure), PaaS (platform), SaaS (software)",
    "Four deployment models: Public, Private, Hybrid, Multi-Cloud",
    "",
    "Key benefits: elasticity, no CapEx, global reach, faster innovation",
    "Key challenges: cost unpredictability, vendor lock-in, compliance, latency",
    "",
    "Modern frontiers:",
    "  •  Edge Computing — low-latency processing near data source",
    "  •  Serverless — run code without managing servers, pay per execution",
    "  •  Cloud-Native — microservices, containers, CI/CD, resilience"
])

# =======================================================
# SLIDE 29: CONCLUSION
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
solid_bg(s, NAVY)
rect(s, Inches(0), Inches(3.5), Inches(13.333), Inches(0.05), BLUE)
txtbox(s, Inches(1), Inches(1.5), Inches(11), Inches(1),
       "The cloud is not a destination — it’s a journey.",
       sz=36, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
txtbox(s, Inches(1), Inches(2.6), Inches(11), Inches(0.8),
       "Companies continuously evolve how they use the cloud.",
       sz=20, color=RGBColor(0xBB,0xCC,0xDD), align=PP_ALIGN.CENTER)
txtbox(s, Inches(1), Inches(4.0), Inches(11), Inches(1.5),
       "Understanding these fundamentals gives you the tools\nto participate in this evolution.",
       sz=22, color=WHITE, align=PP_ALIGN.CENTER)
txtbox(s, Inches(1), Inches(6.0), Inches(11), Inches(0.5),
       "Thank you — Questions?",
       sz=24, color=BLUE, bold=True, align=PP_ALIGN.CENTER)

# =======================================================
# SLIDE 30: THANK YOU
# =======================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
solid_bg(s, NAVY)
txtbox(s, Inches(1), Inches(2.5), Inches(11), Inches(1.5),
       "Thank You", sz=56, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
txtbox(s, Inches(1), Inches(4.0), Inches(11), Inches(1),
       "Any questions?", sz=28, color=BLUE, align=PP_ALIGN.CENTER)

prs.save(str(DST))
print(f"Saved: {DST}")
print(f"Slides: {len(prs.slides)}")
