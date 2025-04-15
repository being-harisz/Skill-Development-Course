{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOp9dRBnQk+7A2dAiA6mv6l"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!pip install -q langchain openai gradio PyMuPDF newspaper3k tiktoken\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z7f0S1byD4tX",
        "outputId": "e23e8f0a-ee65-4954-f50d-11b08ed5f9cb"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m7.4/7.4 MB\u001b[0m \u001b[31m40.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m46.9/46.9 MB\u001b[0m \u001b[31m21.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m322.2/322.2 kB\u001b[0m \u001b[31m25.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m20.0/20.0 MB\u001b[0m \u001b[31m84.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m211.1/211.1 kB\u001b[0m \u001b[31m18.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m60.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m95.2/95.2 kB\u001b[0m \u001b[31m8.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m81.3/81.3 kB\u001b[0m \u001b[31m7.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.4/11.4 MB\u001b[0m \u001b[31m101.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m72.0/72.0 kB\u001b[0m \u001b[31m6.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m106.3/106.3 kB\u001b[0m \u001b[31m9.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.4/62.4 kB\u001b[0m \u001b[31m5.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for tinysegmenter (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for feedfinder2 (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for jieba3k (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for sgmllib3k (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "# Paste your OpenAI API Key here\n",
        "os.environ[\"OPENAI_API_KEY\"] = \"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\"  # Replace with your actual key\n"
      ],
      "metadata": {
        "id": "b7vCownSEFK5"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.chat_models import ChatOpenAI\n",
        "from langchain_core.prompts import ChatPromptTemplate\n",
        "from langchain_core.output_parsers import StrOutputParser\n",
        "\n",
        "# Create LCEL Chain\n",
        "llm = ChatOpenAI(temperature=0.3)\n",
        "prompt = ChatPromptTemplate.from_template(\n",
        "    \"\"\"\n",
        "You are a professional news summarizer. Summarize the following article in 3-5 bullet points:\n",
        "\n",
        "{text}\n",
        "\n",
        "Summary:\n",
        "\"\"\"\n",
        ")\n",
        "chain = prompt | llm | StrOutputParser()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Phw6NI-EELRg",
        "outputId": "48004eba-7341-4a27-ecd7-bb566a109e42"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-10-b78577fa063f>:6: LangChainDeprecationWarning: The class `ChatOpenAI` was deprecated in LangChain 0.0.10 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-openai package and should be used instead. To use it run `pip install -U :class:`~langchain-openai` and import as `from :class:`~langchain_openai import ChatOpenAI``.\n",
            "  llm = ChatOpenAI(temperature=0.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q langchain langchain-openai gradio PyMuPDF newspaper3k tiktoken\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "krU2U552Ed_S",
        "outputId": "fc91596d-cb8c-4f14-9f2f-e5158a42048e"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/61.3 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m61.3/61.3 kB\u001b[0m \u001b[31m2.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "# Replace with your actual OpenAI API key\n",
        "os.environ[\"OPENAI_API_KEY\"] = \"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\"  # Your OpenAI API Key here\n"
      ],
      "metadata": {
        "id": "vGavxXUyEidE"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_openai import ChatOpenAI\n",
        "from langchain.prompts import ChatPromptTemplate\n",
        "\n",
        "# Create LCEL Chain\n",
        "llm = ChatOpenAI(temperature=0.3)\n",
        "prompt = ChatPromptTemplate.from_template(\n",
        "    \"\"\"\n",
        "You are a professional news summarizer. Summarize the following article in 3-5 bullet points:\n",
        "\n",
        "{text}\n",
        "\n",
        "Summary:\n",
        "\"\"\"\n",
        ")\n",
        "chain = prompt | llm\n"
      ],
      "metadata": {
        "id": "Bn7HQPi_E6SL"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import fitz  # PyMuPDF\n",
        "from newspaper import Article\n",
        "\n",
        "def extract_text_from_pdf(file):\n",
        "    doc = fitz.open(stream=file.read(), filetype=\"pdf\")\n",
        "    return \"\\n\".join(page.get_text() for page in doc)\n",
        "\n",
        "def extract_text_from_url(url):\n",
        "    article = Article(url)\n",
        "    article.download()\n",
        "    article.parse()\n",
        "    return article.text\n"
      ],
      "metadata": {
        "id": "G0O-6sqVE-ay"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import gradio as gr\n",
        "\n",
        "def summarize_news(article_text=\"\", pdf_file=None, url=\"\"):\n",
        "    try:\n",
        "        if pdf_file is not None:\n",
        "            article_text = extract_text_from_pdf(pdf_file)\n",
        "        elif url.strip():\n",
        "            article_text = extract_text_from_url(url)\n",
        "\n",
        "        if not article_text.strip():\n",
        "            return \"❗ Please provide a valid article text, PDF, or URL.\"\n",
        "\n",
        "        # Directly invoke the model to get the summary\n",
        "        result = chain.invoke({\"text\": article_text})\n",
        "        return result\n",
        "\n",
        "    except Exception as e:\n",
        "        return f\"❌ Error: {str(e)}\"\n",
        "\n",
        "with gr.Blocks() as demo:\n",
        "    gr.Markdown(\"## 📰 News Summarizer using LangChain + LCEL\")\n",
        "    with gr.Row():\n",
        "        article_input = gr.Textbox(label=\"Paste Article Text\", lines=10, placeholder=\"Or upload PDF / enter URL below...\")\n",
        "    with gr.Row():\n",
        "        pdf_input = gr.File(label=\"Upload PDF\", file_types=[\".pdf\"])\n",
        "        url_input = gr.Textbox(label=\"News Article URL\")\n",
        "    summarize_btn = gr.Button(\"Summarize\")\n",
        "    output = gr.Textbox(label=\"Summary Output\", lines=10)\n",
        "\n",
        "    summarize_btn.click(\n",
        "        summarize_news,\n",
        "        inputs=[article_input, pdf_input, url_input],\n",
        "        outputs=[output]\n",
        "    )\n",
        "\n",
        "demo.launch()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 616
        },
        "id": "durUBsY_FP4e",
        "outputId": "404c8160-08d0-4756-a1f8-296fe9783d23"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Colab notebook detected. To show errors in colab notebook, set debug=True in launch()\n",
            "Note: opening Chrome Inspector may crash demo inside Colab notebooks.\n",
            "\n",
            "To create a public link, set `share=True` in `launch()`.\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "(async (port, path, width, height, cache, element) => {\n",
              "                        if (!google.colab.kernel.accessAllowed && !cache) {\n",
              "                            return;\n",
              "                        }\n",
              "                        element.appendChild(document.createTextNode(''));\n",
              "                        const url = await google.colab.kernel.proxyPort(port, {cache});\n",
              "\n",
              "                        const external_link = document.createElement('div');\n",
              "                        external_link.innerHTML = `\n",
              "                            <div style=\"font-family: monospace; margin-bottom: 0.5rem\">\n",
              "                                Running on <a href=${new URL(path, url).toString()} target=\"_blank\">\n",
              "                                    https://localhost:${port}${path}\n",
              "                                </a>\n",
              "                            </div>\n",
              "                        `;\n",
              "                        element.appendChild(external_link);\n",
              "\n",
              "                        const iframe = document.createElement('iframe');\n",
              "                        iframe.src = new URL(path, url).toString();\n",
              "                        iframe.height = height;\n",
              "                        iframe.allow = \"autoplay; camera; microphone; clipboard-read; clipboard-write;\"\n",
              "                        iframe.width = width;\n",
              "                        iframe.style.border = 0;\n",
              "                        element.appendChild(iframe);\n",
              "                    })(7860, \"/\", \"100%\", 500, false, window.element)"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": []
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q lxml[html_clean]\n"
      ],
      "metadata": {
        "id": "g5hPZvhKFFYi"
      },
      "execution_count": 17,
      "outputs": []
    }
  ]
}