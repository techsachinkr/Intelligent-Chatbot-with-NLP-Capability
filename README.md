# Intelligent-Chatbot-with-NLP-Capability

NLP based chatbot developed duringLexis Nexis Hackathon for answering queries related to LexisNexis Online Help System

Guidelines for running Code:

1.  Install  nltk package with command ‘pip install nltk’
2. Download nltk corpora with line ‘ nltk.download()’, and ‘nltk.download('punkt')’its too  big so choose your packages as you want.
3. Also install flask api ‘pip install flask’
4.  Run ‘app.py’ script and in browser open ‘http://localhost:5002/’
5. Now we are good to go, just type in any query and press enter to get response

Description:
This chatbot answers your query related to navigating three of Lexisnexis modules which are :
Litigation Profile Suite,Lexis Advance Tax,Interactive Citation Workstation

Now how the answer is strcutured:

i) First line you '' get modulename your query is related to.

ii) Third line contains exact url containing the information you asked for.

Demo:

User Said: search for judge

BotResponse: Your question is related to. Litigation Profile Suite
For Detailed step-by-step info you can goto:
http://help.lexisnexis.com/tabula-rasa/newlexis/lpssearchlexisweb_hdi-task?lbu=US&locale=en_US&audience=lps
What else i can help you with now ?
