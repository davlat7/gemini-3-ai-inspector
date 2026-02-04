# 🔍 AI Inspector: Gemini 3 Fix-It Assistant

**AI Inspector** is an intelligent diagnostic tool developed for the **Gemini 3 Hackathon**. It empowers users to solve everyday household problems by simply taking a photo. Powered by **Gemini 2.0 Flash**, it identifies issues (stains, broken gadgets, leaks) and provides immediate, actionable repair guides.

---

## 🎯 Project Overview & Impact (Potential Impact - 20%)
Most people face minor household crises daily—a permanent ink stain on a shirt, a leaking faucet, or a cryptic error code on a microwave. Often, the solution is simple, but the knowledge is missing. 
- **The Problem:** Millions of items are discarded annually due to repairable minor damage, leading to waste and unnecessary expenses.
- **Our Solution:** AI Inspector acts as a "Digital Handyman," saving users time and money while promoting sustainability through the culture of repair.
- **Market Reach:** This tool is globally applicable, helping everyone from busy parents to students maintain their belongings without expensive professional help.

## ⚙️ Technical Execution (Technical Execution - 40%)
Built using the latest AI technology to ensure high performance and reliability:
- **Core LLM:** **Google Gemini 2.0 Flash**. We utilized this model for its native multimodal capabilities and industry-leading inference speed, ensuring near-instant feedback.
- **Frontend:** **Streamlit** was used to build a clean, intuitive, and responsive web interface accessible from any device.
- **Backend:** Developed in **Python 3.10+** utilizing the latest `google-genai` SDK for seamless model interaction.
- **Workflow:** 1. User uploads an image via the Streamlit interface.
  2. The image is processed and sent to the Gemini 2.0 API with a specialized "Repair Expert" system prompt.
  3. Gemini performs **multimodal reasoning** to diagnose the visual problem.
  4. Detailed Markdown-formatted instructions are returned to the user.

## 💡 Innovation & "Wow" Factor (Innovation - 30%)
What sets AI Inspector apart:
- **Native Multimodality:** Unlike traditional visual recognition, Gemini 3 understands context. It doesn't just see a "stain"; it analyzes the fabric texture and the chemical nature of the substance to give a specific cleaning recipe.
- **Visual Intelligence:** It goes beyond description. It predicts the tools and materials needed (e.g., "You will need white vinegar and a microfiber cloth") based on visual evidence.
- **Flash Architecture:** By leveraging the **Flash** model, we achieve real-time expert diagnostics that feel like a live conversation with a technician.

## 🛠️ System Architecture (Presentation/Docs - 10%)

Clone the repository: git clone https://github.com/davlat7/gemini-3-ai-inspector.git

Install dependencies: pip install -r requirements.txt

Run the application: streamlit run "hackathon_gemini.py"

```mermaid
graph TD
    User((User)) -->|Uploads Image| UI[Streamlit Frontend]
    UI -->|Image + Prompt| API[Gemini 2.0 Flash API]
    API -->|Multimodal Reasoning| Engine[Gemini Vision Engine]
    Engine -->|Step-by-Step Guide| UI
    UI -->|Display Solution| User

