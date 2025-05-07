apikey = st.text_input("openai api key를 입력하세요 :", type = "password")

client = OpenAI(api_key=apikey)

@st.cache_data
def what(gg):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": gg}
        ]
    )
    return response.choices[0].message.content




if apikey != "":
    gg = st.text_input("질문하세요:")
    if gg:
        a = what(gg)
        st.write(a)
