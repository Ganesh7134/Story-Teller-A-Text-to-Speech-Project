# Story-Teller-A-Text-to-Speech-Project

## **Project Overview:**
Story Teller is a Python-based project designed to convert images to text descriptions and then translate those descriptions into spoken stories. It utilizes a combination of powerful libraries to achieve this functionality:
* **Hugging Face Image-to-Text Transformer**: This library extracts textual representations from input images.
* **GenerativeAI (Google API)**: This API fuels the story generation process, crafting narratives based on the provided text prompts.
* **gTTS (Google Text-to-Speech)**: This library converts the generated story text into an audio file for playback.
  
## **Functionality**:
1.	**Image Processing**: The application begins by accepting an image as input.
2.	**Text Description Generation**: Utilizing the Hugging Face image-to-text transformer, the project extracts a textual description of the image content.
3.	**Story Generation**: This extracted description serves as the basis for story generation. The GenerativeAI API is invoked using a Google API key, providing the textual prompt and generating a compelling story based on it.
4.	**Text-to-Speech Conversion**: Finally, the generated story text is transformed into an audio file using the gTTS library, allowing you to listen to the story.

## **Conclusion**:
Story Teller demonstrates the potential of combining various AI-powered tools to create engaging and interactive experiences. It leverages cutting-edge technologies to bridge the gap between visual and auditory narratives, opening doors for further exploration in creative AI applications.

