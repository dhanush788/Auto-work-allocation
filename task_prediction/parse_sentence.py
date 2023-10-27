import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import sys

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Sample data for training the classifier
data = [
    # Front End Developer Data
    ("Add a navigation bar and customized footer in website", "Front End Developer"),
    ("Create responsive website layouts.", "Front End Developer"),
    ("Design user interfaces (UI) for web applications.", "Front End Developer"),
    ("Implement user experience (UX) design concepts.", "Front End Developer"),
    ("Develop web pages using HTML and CSS.", "Front End Developer"),
    ("Optimize web assets for performance.", "Front End Developer"),
    ("Add animations and transitions to web elements.", "Front End Developer"),
    ("Integrate JavaScript for interactive web features.", "Front End Developer"),
    ("Implement web accessibility features (e.g., ARIA roles).", "Front End Developer"),
    ("Design and code custom web forms.", "Front End Developer"),
    ("Build and style navigation menus.", "Front End Developer"),
    ("Create and integrate web icons and fonts.", "Front End Developer"),
    ("Work with version control systems (e.g., Git).", "Front End Developer"),
    ("Collaborate with UI/UX designers.", "Front End Developer"),
    ("Perform cross-browser testing and debugging.", "Front End Developer"),
    ("Implement responsive typography.", "Front End Developer"),
    ("Optimize web images and graphics.", "Front End Developer"),
    ("Incorporate video and audio elements into web pages.", "Front End Developer"),
    ("Implement third-party APIs and widgets.", "Front End Developer"),
    ("Design and code email templates.", "Front End Developer"),
    ("Create landing pages for marketing campaigns.", "Front End Developer"),
    ("Build and style interactive carousels and sliders.", "Front End Developer"),
    ("Develop parallax scrolling effects.", "Front End Developer"),
    ("Implement lazy loading for images.", "Front End Developer"),
    ("Integrate social media sharing functionality.", "Front End Developer"),
    ("Create and style web buttons.", "Front End Developer"),
    ("Design and code modals and pop-up windows.", "Front End Developer"),
    ("Develop web-based data visualizations.", "Front End Developer"),
    ("Implement web chat and messaging features.", "Front End Developer"),
    ("Build and style progress bars and loaders.", "Front End Developer"),
    ("Create and maintain style guides and design systems.", "Front End Developer"),
    ("Optimize web forms for user input.", "Front End Developer"),
    ("Implement responsive tables and grids.", "Front End Developer"),
    ("Design and code custom tooltips.", "Front End Developer"),
    ("Integrate content management systems (CMS).", "Front End Developer"),
    ("Develop e-commerce product pages.", "Front End Developer"),
    ("Create and style accordions and tabs.", "Front End Developer"),
    ("Build web-based dashboards and admin interfaces.", "Front End Developer"),
    ("Design and code infographics.", "Front End Developer"),
    ("Develop interactive maps and geolocation features.", "Front End Developer"),
    ("Implement real-time data updates (e.g., live scores).", "Front End Developer"),
    ("Optimize website for mobile devices.", "Front End Developer"),
    ("Integrate web analytics and tracking tools.", "Front End Developer"),
    ("Design and code email subscription forms.", "Front End Developer"),
    ("Create and style progress trackers.", "Front End Developer"),
    ("Develop web games and interactive quizzes.", "Front End Developer"),
    ("Implement client-side routing (e.g., with React Router).", "Front End Developer"),
    ("Design and code drop-down menus.", "Front End Developer"),
    ("Build and style pricing tables.", "Front End Developer"),
    ("Incorporate light and dark theme options.", "Front End Developer"),
    ("Create and style image galleries.", "Front End Developer"),
    ("Implement content sharing via social media.", "Front End Developer"),
    ("Develop responsive carousels for testimonials.", "Front End Developer"),
    ("Design and code custom 404 error pages.", "Front End Developer"),
    ("Optimize web content for SEO.", "Front End Developer"),
    ("Incorporate lazy loading for web fonts.", "Front End Developer"),
    ("Build and style date pickers and calendars.", "Front End Developer"),
    ("Develop and style interactive charts and graphs.", "Front End Developer"),
    ("Implement client-side validation for forms.", "Front End Developer"),
    ("Create web-based calculators and converters.", "Front End Developer"),
    ("Design and code sticky headers and sidebars.", "Front End Developer"),
    ("Build and style mega menus.", "Front End Developer"),
    ("Incorporate geospatial and mapping features.", "Front End Developer"),
    ("Optimize website for print (print stylesheets).", "Front End Developer"),
    ("Integrate search functionality.", "Front End Developer"),
    ("Develop web-based surveys and feedback forms.", "Front End Developer"),
    ("Create and style image carousels with thumbnails.", "Front End Developer"),
    ("Implement user profile and account pages.", "Front End Developer"),
    ("Design and code custom web banners.", "Front End Developer"),
    ("Build and style timeline and history features.", "Front End Developer"),
    ("Incorporate web-based notification systems.", "Front End Developer"),
    ("Develop interactive educational content.", "Front End Developer"),
    ("Optimize web content for voice search.", "Front End Developer"),
    ("Integrate web-based file uploads and downloads.", "Front End Developer"),
    ("Design and code step-by-step tutorials.", "Front End Developer"),
    ("Create and style accordions and FAQs.", "Front End Developer"),
    ("Build and style voting and polling systems.", "Front End Developer"),
    ("Implement interactive storytelling features.", "Front End Developer"),
    ("Develop web-based job boards and listings.", "Front End Developer"),
    ("Design and code social network profiles.", "Front End Developer"),
    ("Optimize website for accessibility and screen readers.", "Front End Developer"),
    ("Incorporate user-generated content features.", "Front End Developer"),
    ("Create and style product review and rating systems.", "Front End Developer"),
    ("Build web-based calculators for financial planning.", "Front End Developer"),
    ("Implement live chat support widgets.", "Front End Developer"),
    ("Develop and style event calendars.", "Front End Developer"),
    ("Integrate web-based booking and reservation systems.", "Front End Developer"),
    ("Design and code interactive decision trees.", "Front End Developer"),
    ("Optimize web content for internationalization (i18n).", "Front End Developer"),
    ("Incorporate user authentication and login features.", "Front End Developer"),
    ("Create and style web-based newsletters.", "Front End Developer"),
    ("Build and style web surveys and quizzes.", "Front End Developer"),
    ("Implement online ordering and checkout processes.", "Front End Developer"),
    ("Develop and style weather and location widgets.", "Front End Developer"),
    ("Integrate e-learning and course platforms.", "Front End Developer"),
    ("Design and code online forums and discussion boards.", "Front End Developer"),
    ("Optimize website for slow connections (progressive enhancement).", "Front End Developer"),
    ("Incorporate web-based data reporting and visualization.", "Front End Developer"),
    ("Create and style custom video players.", "Front End Developer"),
    ("Build and style knowledge bases and wikis.", "Front End Developer"),
    ("Implement user-generated content moderation tools.", "Front End Developer"),

    # Back End Developer data
    ("Design and develop server-side applications.", "Back End Developer"),
    ("Create RESTful or GraphQL APIs.", "Back End Developer"),
    ("Implement database models and schemas.", "Back End Developer"),
    ("Optimize database queries and performance.", "Back End Developer"),
    ("Handle user authentication and authorization.", "Back End Developer"),
    ("Secure web applications against common vulnerabilities.", "Back End Developer"),
    ("Work with web frameworks (e.g., Django, Ruby on Rails).", "Back End Developer"),
    ("Develop and manage server infrastructure (e.g., AWS, Azure).", "Back End Developer"),
    ("Integrate third-party services and APIs.", "Back End Developer"),
    ("Implement caching mechanisms (e.g., Redis).", "Back End Developer"),
    ("Design and build data migration scripts.", "Back End Developer"),
    ("Develop and maintain background jobs and queues.", "Back End Developer"),
    ("Handle session management and cookies.", "Back End Developer"),
    ("Create and manage application logs and monitoring.", "Back End Developer"),
    ("Implement real-time data synchronization (e.g., WebSockets).", "Back End Developer"),
    ("Set up and manage web servers (e.g., Apache, Nginx).", "Back End Developer"),
    ("Build and maintain REST documentation (e.g., Swagger).", "Back End Developer"),
    ("Optimize application for scalability and high traffic.", "Back End Developer"),
    ("Design and develop microservices architectures.", "Back End Developer"),
    ("Work with containerization and orchestration (e.g., Docker, Kubernetes).", "Back End Developer"),
    ("Implement data backup and disaster recovery solutions.", "Back End Developer"),
    ("Develop payment processing and e-commerce features.", "Back End Developer"),
    ("Create and manage user profiles and accounts.", "Back End Developer"),
    ("Build and maintain APIs for mobile app integration.", "Back End Developer"),
    ("Design and build search functionality (e.g., Elasticsearch).", "Back End Developer"),
    ("Handle versioning and backward compatibility for APIs.", "Back End Developer"),
    ("Integrate single sign-on (SSO) solutions.", "Back End Developer"),
    ("Develop content management systems (CMS).", "Back End Developer"),
    ("Design and implement scheduled tasks and cron jobs.", "Back End Developer"),
    ("Optimize application for multi-threading and concurrency.", "Back End Developer"),
    ("Implement geospatial and mapping features.", "Back End Developer"),
    ("Build and maintain email notification systems.", "Back End Developer"),
    ("Create and manage custom error handling and reporting.", "Back End Developer"),
    ("Integrate and manage message queues (e.g., RabbitMQ).", "Back End Developer"),
    ("Develop and maintain webhooks for third-party services.", "Back End Developer"),
    ("Design and build data analytics and reporting tools.", "Back End Developer"),
    ("Implement authentication with OAuth or OpenID Connect.", "Back End Developer"),
    ("Set up and manage load balancing for web servers.", "Back End Developer"),
    ("Create and manage web security policies and firewalls.", "Back End Developer"),
    ("Build and maintain content delivery networks (CDN).", "Back End Developer"),
    ("Optimize application for SEO and structured data.", "Back End Developer"),
    ("Integrate and manage payment gateways (e.g., Stripe).", "Back End Developer"),
    ("Develop and maintain chat and messaging features.", "Back End Developer"),
    ("Design and implement access control lists (ACL).", "Back End Developer"),
    ("Handle data import and export processes.", "Back End Developer"),
    ("Build and maintain automated testing frameworks.", "Back End Developer"),
    ("Implement server-side rendering (SSR).", "Back End Developer"),
    ("Create and manage serverless functions (e.g., AWS Lambda).", "Back End Developer"),
    ("Design and develop web scrapers and crawlers.", "Back End Developer"),
    ("Optimize application for compliance (e.g., GDPR).", "Back End Developer"),
    ("Integrate and manage NoSQL databases (e.g., MongoDB).", "Back End Developer"),
    ("Develop and maintain REST or SOAP integrations.", "Back End Developer"),
    ("Set up and manage continuous integration and deployment (CI/CD).", "Back End Developer"),
    ("Implement file and media storage solutions (e.g., Amazon S3).", "Back End Developer"),
    ("Design and build subscription billing systems.", "Back End Developer"),
    ("Handle email delivery and newsletters.", "Back End Developer"),
    ("Create and maintain API rate limiting and throttling.", "Back End Developer"),
    ("Develop and maintain content recommendation algorithms.", "Back End Developer"),
    ("Optimize application for asynchronous processing.", "Back End Developer"),
    ("Integrate and manage identity and access management (IAM).", "Back End Developer"),
    ("Design and build online forms and surveys.", "Back End Developer"),
    ("Implement and manage database backups and replication.", "Back End Developer"),
    ("Set up and manage custom domain routing and DNS.", "Back End Developer"),
    ("Create and maintain code version control (e.g., Git).", "Back End Developer"),
    ("Build and manage software containers and images.", "Back End Developer"),
    ("Design and implement real-time analytics and dashboards.", "Back End Developer"),
    ("Handle user account provisioning and deprovisioning.", "Back End Developer"),
    ("Develop and maintain web-based administration panels.", "Back End Developer"),
    ("Optimize application for cross-device compatibility.", "Back End Developer"),
    ("Integrate and manage social media authentication.", "Back End Developer"),
    ("Create and maintain automated error reporting and alerts.", "Back End Developer"),
    ("Implement and manage in-app notifications.", "Back End Developer"),
    ("Design and develop content personalization features.", "Back End Developer"),
    ("Build and maintain e-learning platforms.", "Back End Developer"),
    ("Handle application security and vulnerability scanning.", "Back End Developer"),
    ("Develop and maintain custom search engines.", "Back End Developer"),
    ("Optimize application for data privacy and encryption.", "Back End Developer"),
    ("Integrate and manage machine learning and AI services.", "Back End Developer"),
    ("Create and manage API key authentication.", "Back End Developer"),
    ("Design and implement event-driven architectures.", "Back End Developer"),
    ("Build and maintain online booking and reservation systems.", "Back End Developer"),
    ("Implement and manage application performance monitoring.", "Back End Developer"),
    ("Set up and manage reverse proxies and caching servers.", "Back End Developer"),
    ("Develop and maintain server-side ad placements.", "Back End Developer"),
    ("Handle server health monitoring and reporting.", "Back End Developer"),
    ("Create and maintain data streaming and processing.", "Back End Developer"),
    ("Design and build content distribution platforms.", "Back End Developer"),
    ("Optimize application for serverless computing.", "Back End Developer"),
    ("Integrate and manage IoT and sensor data.", "Back End Developer"),
    ("Develop and maintain financial and accounting systems.", "Back End Developer"),
    ("Implement and manage session-based authentication.", "Back End Developer"),
    ("Set up and manage data warehousing and analytics.", "Back End Developer"),
    ("Create and maintain custom e-commerce platforms.", "Back End Developer"),
    ("Build and maintain content syndication networks.", "Back End Developer"),
    ("Design and implement custom content workflows.", "Back End Developer"),
    ("Develop and maintain online gaming platforms.", "Back End Developer"),
    ("Optimize application for data storage and retrieval.", "Back End Developer"),
    ("Integrate and manage blockchain and cryptocurrency features.", "Back End Developer"),
    ("Handle integration with content delivery platforms (CDP).", "Back End Developer"),
    ("Implement and manage disaster recovery and backups.", "Back End Developer"),
    ("Optimize database queries for performance", "Back End Developer"),

    # Systems programmer
    ("Develop and maintain operating system components.", "Systems Programmer"),
    ("Create device drivers for hardware peripherals.", "Systems Programmer"),
    ("Optimize system performance and resource utilization.", "Systems Programmer"),
    ("Debug and troubleshoot low-level system issues.", "Systems Programmer"),
    ("Design and implement system-level security measures.", "Systems Programmer"),
    ("Work with kernel development and modification.", "Systems Programmer"),
    ("Develop custom file systems or file system drivers.", "Systems Programmer"),
    ("Optimize memory management and allocation.", "Systems Programmer"),
    ("Create and maintain system-level APIs and libraries.", "Systems Programmer"),
    ("Implement and maintain system-level concurrency.", "Systems Programmer"),
    ("Design and build embedded system firmware.", "Systems Programmer"),
    ("Optimize real-time system responsiveness.", "Systems Programmer"),
    ("Develop and maintain system initialization scripts.", "Systems Programmer"),
    ("Integrate system monitoring and logging.", "Systems Programmer"),
    ("Design and implement low-level networking protocols.", "Systems Programmer"),
    ("Optimize system power management.", "Systems Programmer"),
    ("Work with system-level virtualization (e.g., VMs, containers).", "Systems Programmer"),
    ("Develop and maintain firmware for microcontrollers.", "Systems Programmer"),
    ("Create and manage bootloader and BIOS code.", "Systems Programmer"),
    ("Optimize system resource allocation for virtualization.", "Systems Programmer"),
    ("Design and build system-level communication protocols.", "Systems Programmer"),
    ("Implement and manage system recovery mechanisms.", "Systems Programmer"),
    ("Optimize system performance for multiple processors (SMP).", "Systems Programmer"),
    ("Develop and maintain system-level fault tolerance.", "Systems Programmer"),
    ("Work with low-level hardware control and interfacing.", "Systems Programmer"),
    ("Create and maintain system-level package managers.", "Systems Programmer"),
    ("Optimize system security and access controls.", "Systems Programmer"),
    ("Implement and manage system-level backups and restores.", "Systems Programmer"),
    ("Design and build custom system-level scripting languages.", "Systems Programmer"),
    ("Develop and maintain custom system utilities.", "Systems Programmer"),
    ("Optimize system-level support for distributed computing.", "Systems Programmer"),
    ("Integrate and manage software-defined networking (SDN).", "Systems Programmer"),
    ("Work with low-level cryptography and encryption.", "Systems Programmer"),
    ("Create and maintain firmware for IoT devices.", "Systems Programmer"),
    ("Optimize system-level support for edge computing.", "Systems Programmer"),
    ("Design and implement real-time operating systems (RTOS).", "Systems Programmer"),
    ("Develop and maintain system-level disaster recovery plans.", "Systems Programmer"),
    ("Optimize system-level support for cloud computing.", "Systems Programmer"),
    ("Work with system-level authentication mechanisms.", "Systems Programmer"),
    ("Implement and manage system-level version control systems.", "Systems Programmer"),
    ("Design and build custom system-level databases.", "Systems Programmer"),
    ("Develop and maintain system-level scripting interpreters.", "Systems Programmer"),
    ("Optimize system-level support for high-performance computing (HPC).", "Systems Programmer"),
    ("Create and maintain system-level automated testing frameworks.", "Systems Programmer"),
    ("Integrate and manage system-level IoT platforms.", "Systems Programmer"),
    ("Work with low-level storage protocols (e.g., NVMe).", "Systems Programmer"),
    ("Optimize system-level support for data warehousing.", "Systems Programmer"),
    ("Develop and maintain system-level compliance frameworks.", "Systems Programmer"),
    ("Design and implement embedded system diagnostics.", "Systems Programmer"),
    ("Implement and manage real-time data processing systems.", "Systems Programmer"),
    ("Optimize system-level support for distributed databases.", "Systems Programmer"),
    ("Work with low-level graphics and GPU programming.", "Systems Programmer"),
    ("Create and maintain system-level documentation and manuals.", "Systems Programmer"),
    ("Develop and maintain system-level orchestration tools.", "Systems Programmer"),
    ("Optimize system-level support for machine learning and AI.", "Systems Programmer"),
    ("Design and implement custom system-level communication stacks.", "Systems Programmer"),
    ("Implement and manage system-level code analysis and profiling.", "Systems Programmer"),
    ("Develop and maintain system-level data visualization tools.", "Systems Programmer"),
    ("Optimize system-level support for quantum computing.", "Systems Programmer"),
    ("Work with low-level sensor and IoT device integration.", "Systems Programmer"),
    ("Create and maintain system-level continuous integration (CI) pipelines.", "Systems Programmer"),
    ("Develop and maintain system-level automation and scripting tools.", "Systems Programmer"),
    ("Optimize system-level support for edge AI and IoT.", "Systems Programmer"),
    ("Design and build system-level data analytics platforms.", "Systems Programmer"),
    ("Implement and manage system-level data security solutions.", "Systems Programmer"),
    ("Optimize system-level support for serverless computing.", "Systems Programmer"),
    ("Work with low-level robotics and automation systems.", "Systems Programmer"),
    ("Develop and maintain system-level code generators.", "Systems Programmer"),
    ("Create and manage system-level configuration management tools.", "Systems Programmer"),
    ("Design and implement system-level software-defined radios.", "Systems Programmer"),
    ("Implement and manage system-level machine learning frameworks.", "Systems Programmer"),
    ("Optimize system-level support for blockchain technology.", "Systems Programmer"),
    ("Work with low-level hardware security modules (HSMs).", "Systems Programmer"),
    ("Develop and maintain system-level content delivery networks (CDN).", "Systems Programmer"),
    ("Create and maintain system-level data mining and analytics solutions.", "Systems Programmer"),
    ("Optimize system-level support for distributed ledger technology.", "Systems Programmer"),
    ("Design and build custom system-level development environments.", "Systems Programmer"),
    ("Implement and manage system-level natural language processing (NLP).", "Systems Programmer"),
    ("Optimize system-level support for the Internet of Things (IoT).", "Systems Programmer"),
    ("Work with low-level quantum computing platforms.", "Systems Programmer"),
    ("Develop and maintain system-level augmented reality (AR) frameworks.", "Systems Programmer"),
    ("Create and manage system-level artificial intelligence (AI) platforms.", "Systems Programmer"),
    ("Optimize system-level support for 5G and wireless networking.", "Systems Programmer"),
    ("Design and implement system-level autonomous vehicle control systems.", "Systems Programmer"),
    ("Implement and manage system-level genomics and bioinformatics solutions.", "Systems Programmer"),
    ("Optimize system-level support for cybersecurity and threat detection.", "Systems Programmer"),
    ("Work with low-level nanotechnology and materials science.", "Systems Programmer"),
    ("Develop and maintain system-level autonomous robotics and drones.", "Systems Programmer"),
    ("Create and maintain system-level quantum computing languages and compilers.", "Systems Programmer"),
    ("Design and build custom system-level virtual reality (VR) platforms.", "Systems Programmer"),
    ("Implement and manage system-level natural resource management solutions.", "Systems Programmer"),
    ("Optimize system-level support for space exploration and satellite systems.", "Systems Programmer"),
    ("Work with low-level fusion and clean energy technologies.", "Systems Programmer"),
    ("Develop and maintain system-level autonomous agriculture and farming systems.", "Systems Programmer"),
    ("Create and manage system-level environmental monitoring and conservation solutions.", "Systems Programmer"),
    ("Optimize system-level support for biotechnology and pharmaceutical research.", "Systems Programmer"),
    ("Design and implement system-level climate modeling and environmental simulations.", "Systems Programmer"),
    ("Implement and manage system-level computational fluid dynamics (CFD) and simulations.", "Systems Programmer"),
    ("Optimize system-level support for nuclear technology and fusion energy.", "Systems Programmer"),
    ("Work with low-level research and development of emerging technologies.", "Systems Programmer")

    # Add more training examples with task descriptions and corresponding developer types
]

# Tokenize and preprocess the text data
texts, labels = zip(*data)
tokenized_texts = [nlp(text) for text in texts]

# Feature extraction using Bag of Words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train a simple text classifier (Multinomial Naive Bayes)
clf = MultinomialNB()
clf.fit(X, labels)

def determine_developer_type(task_description):
    # Tokenize and preprocess the task description
    task_doc = nlp(task_description)
    # Convert the text into a Bag of Words representation
    task_vector = vectorizer.transform([task_description])
    # Predict the developer type
    developer_type = clf.predict(task_vector)[0]
    return developer_type

task_description = sys.argv[1]
developer_type = determine_developer_type(task_description)
print(f"Assign the task to a {developer_type}.")
