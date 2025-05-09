
import streamlit as st

st.set_page_config(page_title="ماشین‌حساب ریسک و لوریج", layout="centered")

st.title("📊 ماشین‌حساب مدیریت ریسک و لوریج بازار فیوچرز")

st.markdown("با استفاده از این ابزار می‌توانید اندازه پوزیشن، مارجین لازم، سود بالقوه و میزان ریسک را محاسبه کنید.")

balance = st.number_input("💰 موجودی کل حساب (تتر)", min_value=1.0, value=1000.0, step=10.0)
risk_percent = st.slider("🎯 درصد ریسک در هر معامله (%)", 0.1, 100.0, 2.0)
entry_price = st.number_input("🔹 قیمت ورود (تتر)", min_value=0.01, value=100.0)
stop_loss_price = st.number_input("🔻 قیمت حد ضرر (تتر)", min_value=0.01, value=95.0)
take_profit_price = st.number_input("🟢 قیمت هدف سود (تتر)", min_value=0.01, value=110.0)
leverage = st.slider("🧮 میزان لوریج (برابر)", 1, 125, 10)
fee_percent = st.number_input("💸 مجموع کارمزد ورود و خروج (%)", min_value=0.0, value=0.1)

risk_amount = balance * (risk_percent / 100)
risk_per_unit = abs(entry_price - stop_loss_price)
position_size = risk_amount / risk_per_unit if risk_per_unit else 0
notional_value = position_size * entry_price
adjusted_margin = notional_value / leverage
fees = notional_value * (fee_percent / 100)
profit_potential = (take_profit_price - entry_price) * position_size

st.subheader("🔍 نتایج محاسبه:")

st.write(f"📌 میزان سرمایه در ریسک: **{risk_amount:.2f} تتر**")
st.write(f"📌 حجم پیشنهادی پوزیشن: **{position_size:.4f} واحد**")
st.write(f"📌 ارزش کل معامله (بدون لوریج): **{notional_value:.2f} تتر**")
st.write(f"📌 مارجین مورد نیاز (با لوریج {leverage}×): **{adjusted_margin:.2f} تتر**")
st.write(f"📌 مجموع کارمزد تخمینی: **{fees:.2f} تتر**")
st.write(f"📌 سود احتمالی (قبل از کارمزد): **{profit_potential:.2f} تتر**")
