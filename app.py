import streamlit as st
import math
import pandas as pd
import plotly.express as px
from io import BytesIO
from fpdf import FPDF

# ============================
# Configuración de la Página
# ============================
st.set_page_config(
    page_title="🚀 Simulador y Curso de CETES",
    layout="wide",
    page_icon="💹"
)

# Función para generar PDF usando fpdf
def generar_pdf(resultados: dict) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Simulación de Inversión en CETES", ln=True, align="C")
    pdf.ln(8)
    pdf.set_font("Arial", "", 12)
    # Recorremos cada resultado y lo agregamos al PDF en dos columnas
    for key, value in resultados.items():
        pdf.cell(60, 10, f"{key}:", border=1)
        pdf.cell(0, 10, f"{value}", border=1, ln=True)
    # Retornamos el PDF como bytes
    return pdf.output(dest="S").encode("latin1")

# ============================
# Pestañas Principales
# ============================
tabs = st.tabs(["📚 Curso de CETES: Explicación Integral", "💰 Simulador de Inversión en CETES"])

# ====================================================
# Pestaña 1: Curso de CETES – Explicación Integral
# ====================================================
with tabs[0]:
    st.title("Curso de CETES: Explicación Integral 📚")
    st.markdown("---")
    
    # Introducción didáctica
    st.markdown("Bienvenido a este curso integral sobre **CETES**. A continuación, encontrarás una explicación detallada de cada concepto clave, acompañada de ejemplos y fórmulas matemáticas. ¡Acompáñanos y descubre cómo funcionan estos instrumentos financieros! 😊")
    st.markdown("---")
    
    # 1. ¿Qué es un CETE?
    st.header("1. ¿Qué es un CETE? 🤔")
    st.markdown(
        "Los **CETES** (Certificados de la Tesorería de la Federación) son instrumentos de deuda a corto plazo emitidos por el gobierno mexicano para financiar sus operaciones. "
        "Se emiten con vencimientos de **28, 91, 182 o 364 días** y tienen un valor nominal de **$10 MXN** por título. "
        "Este instrumento permite a los inversionistas obtener rendimientos en un plazo determinado, siendo una alternativa segura y respaldada por el gobierno."
    )
    st.markdown("---")
    
    # 2. Valor Nominal
    st.header("2. Valor Nominal 💵")
    st.markdown("**Concepto:** Es el valor que se recibirá al vencimiento del título.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Valor Nominal} = 10 \text{ MXN}")
    with st.expander("Ejemplo de Valor Nominal"):
        st.markdown("Cada CETE tiene un valor nominal fijo de **$10 MXN**, que es lo que se recibe al vencimiento del certificado.")
    st.markdown("---")
    
    # 3. Precio de Compra
    st.header("3. Precio de Compra 🛒")
    st.markdown("**Concepto:** Precio al que se adquiere el CETE, obtenido al descontar el valor nominal mediante la tasa de descuento aplicada durante el plazo de la inversión.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Precio de Compra} = \text{Valor Nominal} \times \left(1 - \frac{\text{Tasa de Descuento}}{360} \times \text{Días}\right)")
    with st.expander("Ejemplo de Precio de Compra"):
        st.markdown("Con un Valor Nominal de **$10 MXN**, una Tasa de Descuento de **9.02%** y un plazo de **28 días**:")
        st.latex(r"\text{Precio de Compra} = 10 \times \left(1 - \frac{0.0902}{360} \times 28\right) \approx 9.92984 \text{ MXN}")
    st.markdown("---")
    
    # 4. Remanente
    st.header("4. Remanente 💰")
    st.markdown("**Concepto:** Capital no utilizado en la compra de títulos enteros, que se devuelve al inversor.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Remanente} = \text{Monto a Invertir} - (\text{Número de Títulos} \times \text{Precio de Compra})")
    with st.expander("Ejemplo de Remanente"):
        st.markdown("Si el monto a invertir es de **$400,000 MXN** y el precio de compra de cada CETE es de **$9.92984 MXN**, se compra el máximo número de títulos enteros y el sobrante se considera remanente.")
    st.markdown("---")
    
    # 5. Interés Bruto
    st.header("5. Interés Bruto 📈")
    st.markdown("**Concepto:** Ganancia total sin deducción de impuestos, calculada como la diferencia entre el valor nominal y el precio de compra, multiplicada por el número de títulos adquiridos.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Interés Bruto} = \text{Número de Títulos} \times (\text{Valor Nominal} - \text{Precio de Compra})")
    with st.expander("Ejemplo de Interés Bruto"):
        st.markdown("Si se adquieren **N** títulos, el interés bruto se obtiene multiplicando la diferencia entre **$10 MXN** y el precio de compra por **N**.")
    st.markdown("---")
    
    # 6. ISR (Impuesto Sobre la Renta)
    st.header("6. ISR (Impuesto Sobre la Renta) 💸")
    st.markdown("**Concepto:** Porcentaje que se retiene sobre el interés bruto como impuesto, reduciendo la ganancia final del inversor.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{ISR} = \text{Interés Bruto} \times \frac{\text{Tasa de ISR}}{100}")
    with st.expander("Ejemplo de ISR"):
        st.markdown("Con una tasa de ISR del **5%**, el impuesto se calcula como el **5%** del interés bruto obtenido.")
    st.markdown("---")
    
    # 7. Interés Neto
    st.header("7. Interés Neto 💵➡️💰")
    st.markdown("**Concepto:** Ganancia final después de deducir el ISR del interés bruto.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Interés Neto} = \text{Interés Bruto} - \text{ISR}")
    with st.expander("Ejemplo de Interés Neto"):
        st.markdown("Si el interés bruto es **X MXN** y el ISR es **Y MXN**, el interés neto es **X - Y MXN**.")
    st.markdown("---")
    
    # 8. Rendimientos
    st.header("8. Rendimientos 📊")
    st.markdown("**Concepto:** Indicadores que miden la rentabilidad de la inversión. Se calculan de la siguiente forma:")
    
    st.markdown("**Rendimiento Nominal:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Rendimiento Nominal} = \left(\frac{\text{Valor Nominal}}{\text{Precio de Compra}} - 1\right) \times 100")
    with st.expander("Ejemplo de Rendimiento Nominal"):
        st.markdown("Si el precio de compra es menor que el valor nominal, el rendimiento nominal será positivo y se expresa en porcentaje.")
    
    st.markdown("**Rendimiento Neto:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Rendimiento Neto} = \text{Rendimiento Nominal} - \frac{\text{Tasa de ISR}}{100}")
    with st.expander("Ejemplo de Rendimiento Neto"):
        st.markdown("Se calcula el rendimiento nominal y se le descuenta el efecto del ISR.")
    
    st.markdown("**Rendimiento Real:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Rendimiento Real} = \text{Rendimiento Neto} - \text{Tasa de Inflación}")
    with st.expander("Ejemplo de Rendimiento Real"):
        st.markdown("Se ajusta el rendimiento neto restándole la tasa de inflación para reflejar la ganancia real en términos de poder adquisitivo.")
    st.markdown("---")
    
    # 9. Rendimientos Anualizados
    st.header("9. Rendimientos Anualizados 📆")
    st.markdown("**Concepto:** Proyección del rendimiento a un año, que permite comparar inversiones de distintos plazos.")
    st.markdown("**Fórmula para Rendimiento Nominal Anualizado:**")
    st.latex(r"\text{Rendimiento Nominal Anualizado} = \left[\left(1 + \frac{\text{Rendimiento Nominal}}{100}\right)^{\frac{360}{\text{Días}}} - 1\right] \times 100")
    with st.expander("Ejemplo de Rendimiento Nominal Anualizado"):
        st.markdown("Se utiliza la fórmula para convertir el rendimiento obtenido en el plazo dado a una base anual.")
    st.markdown("---")
    
    # 10. Utilidades Totales
    st.header("10. Utilidades Totales 🏦")
    st.markdown("**Concepto:** Ganancia total obtenida, que incluye el capital invertido y el interés bruto, menos el ISR.")
    st.markdown("**Fórmulas:**")
    st.latex(r"\text{Utilidad Bruta} = \text{Monto Invertido} + \text{Interés Bruto}")
    st.latex(r"\text{Utilidad Real (Principal)} = \text{Utilidad Bruta} - \text{ISR} - \text{Monto Invertido}")
    with st.expander("Ejemplo de Utilidades Totales"):
        st.markdown("Se suma el monto invertido y el interés bruto para obtener la utilidad bruta, y luego se descuenta el ISR para obtener la utilidad real.")
    st.markdown("---")
    
    # 11. Venta Anticipada: Cálculos y Variables
    st.header("11. Venta Anticipada: Cálculos y Variables ⏳")
    st.markdown("**Concepto:** Cálculos que se aplican cuando el CETE se vende antes de su vencimiento, utilizando la tasa de descuento actual.")
    
    st.markdown("**Precio de Venta en Venta Anticipada:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Precio de Venta} = \text{Valor Nominal} \times \left(1 - \frac{\text{Tasa de Descuento Actual}}{360} \times \text{Días Restantes}\right)")
    with st.expander("Ejemplo de Precio de Venta en Venta Anticipada"):
        st.markdown("Si restan **20 días** para el vencimiento y se utiliza la tasa de descuento actual para calcular el precio de venta, se obtiene el valor de mercado del título.")
    
    st.markdown("**Ganancia de Venta:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Ganancia de Venta} = \text{Precio de Venta} - \text{Precio de Compra}")
    with st.expander("Ejemplo de Ganancia de Venta"):
        st.markdown("La ganancia se determina calculando la diferencia entre el precio de venta y el precio de compra.")
    
    st.markdown("**Interés Bruto en Venta Anticipada:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Interés Bruto (Anticipado)} = \text{Número de Títulos} \times \text{Ganancia de Venta}")
    with st.expander("Ejemplo de Interés Bruto en Venta Anticipada"):
        st.markdown("Multiplicando la ganancia de venta por el número de títulos se obtiene el interés bruto anticipado.")
    
    st.markdown("**Rendimientos en Venta Anticipada:**")
    st.markdown("**Fórmulas:**")
    st.latex(r"\text{Rendimiento Nominal (Periodo)} = \frac{\text{Ganancia de Venta}}{\text{Precio de Compra}} \times 100")
    st.latex(r"\text{Rendimiento Neto (Periodo)} = \text{Rendimiento Nominal (Periodo)} - \frac{\text{Tasa de ISR}}{100}")
    st.latex(r"\text{Rendimiento Real (Periodo)} = \text{Rendimiento Neto (Periodo)} - \text{Tasa de Inflación}")
    st.markdown("**Rendimiento Anualizado en Venta Anticipada:**")
    st.latex(r"\text{Rendimiento Anualizado} = \frac{\text{Ganancia de Venta} \times 360}{\text{Precio de Compra} \times \text{Días Transcurridos}} \times 100")
    with st.expander("Ejemplo de Rendimientos en Venta Anticipada"):
        st.markdown("Se calculan los rendimientos para el período transcurrido y se anualizan para poder comparar con otras inversiones.")
    st.markdown("---")
    

# ====================================================
# Pestaña 2: Simulador de Inversión en CETES
# ====================================================
with tabs[1]:
    st.title("💰 Simulador de Inversión en CETES 💰")
    st.markdown("🚀 Ajusta los parámetros a continuación y observa los resultados de tu inversión en CETES. ¡Diviértete y aprende! 😎")
    st.markdown("---")
    
    st.header("📊 Parámetros de la Inversión 📊")
    
    # MONTO A INVERTIR
    monto_total = st.number_input(
        "Monto Total a Invertir (MXN) 💵",
        min_value=1000.0, value=400000.0, step=500.0,
        help="Ingresa el monto total que deseas invertir en CETES."
    )
    
    # PLAZO
    monto_cetes = monto_total
    dias_validos = [28, 91, 182, 365]
    dias = st.select_slider(
        "Plazo de Inversión (días) ⏱️",
        options=dias_validos,
        help="Selecciona el plazo de tu inversión: 28, 91, 182 o 364 días."
    )
    
    # TASA DE DESCUENTO
    tdd_percent = st.number_input(
        "Tasa de Descuento (%) 📉",
        min_value=0.1, max_value=15.0, value=9.2015, step=0.00000001, format="%.8f",
        help="Ingresa la tasa anualizada de descuento para CETES con máxima precisión."
    )
    tdd = tdd_percent / 100.0
    
    # ISR E INFLACIÓN
    st.subheader("🔹 Parámetros Fiscales y Económicos 🔹")
    inflacion = st.number_input(
        "Tasa de Inflación (%) 📈",
        min_value=0.0, max_value=20.0, value=3.77, step=0.00000001, format="%.8f",
        help="Ejemplo: 3.77% medido el 28/03/2025"
    )
    
    isr_percent = st.number_input(
        "Tasa de ISR Aplicada (%) 💸",
        min_value=0.0, max_value=16.0, value=5.0, step=0.00000001, format="%.8f",
        help="Ingresa la tasa de retención del ISR que se aplicará sobre el rendimiento obtenido."
    )
    
    # --- Parámetros para Venta Anticipada ---
    venta_anticipada = st.checkbox(
        "Simular Venta Anticipada (Antes del Vencimiento) ⏳",
        help="Activa esta opción para simular la venta del CETE antes de su vencimiento."
    )
    
    if venta_anticipada:
        dias_transcurridos = st.number_input(
            "Días Transcurridos (antes de la venta) 🕒",
            min_value=1, max_value=dias-1, value=35, step=1,
            help="Ingresa el número de días transcurridos antes de realizar la venta anticipada."
        )
        dias_restantes = dias - dias_transcurridos
        tdd_actual_percent = st.number_input(
            "Tasa de CETES Actual para Venta (%) 🔄",
            min_value=0.1, max_value=30.0, value=tdd_percent, step=0.00000001, format="%.8f",
            help="Ingresa la tasa de descuento vigente para el CETE en el momento de la venta."
        )
        tdd_actual = tdd_actual_percent / 100.0
    else:
        dias_transcurridos = None
        dias_restantes = None
        tdd_actual = None
    
    # --- CÁLCULOS DE RENDIMIENTOS, TASAS E INTERESES ---
    st.markdown("---")
    st.header("💰 Resultados de la Inversión 💰")
    
    # Valor Nominal del CETE
    VN_CETES = 10.0
    
    # Precio de compra calculado con la tasa de descuento original
    precio_cetes = VN_CETES * (1 - (tdd / 360) * dias)
    
    # Número de títulos comprados (solo se adquieren títulos enteros)
    titulos_cetes = math.floor(monto_cetes / precio_cetes)
    inversion_cetes = titulos_cetes * precio_cetes
    remanente_cetes = monto_cetes - inversion_cetes
    
    # Interés Bruto del periodo completo
    interes_bruto_cetes = titulos_cetes * (VN_CETES - precio_cetes)
    isr_cetes = interes_bruto_cetes * (isr_percent / 100.0)
    interes_neto_cetes = interes_bruto_cetes - isr_cetes
    
    # Rendimientos del CETE (Periodo Completo)
    rendimiento_nominal_cetes = ((VN_CETES / precio_cetes) - 1) * 100 if inversion_cetes > 0 else 0
    rendimiento_neto_cetes = rendimiento_nominal_cetes - (isr_percent / 100.0) if inversion_cetes > 0 else 0
    rendimiento_real_cetes = rendimiento_neto_cetes - inflacion
    
    # Rendimientos Anualizados
    rendimiento_nominal_cetes_anual = ((1 + (rendimiento_nominal_cetes / 100)) ** (360 / dias) - 1) * 100 if inversion_cetes > 0 else 0
    rendimiento_neto_cetes_anual = rendimiento_nominal_cetes_anual - (isr_percent / 100.0) if inversion_cetes > 0 else 0
    rendimiento_real_cetes_anual = rendimiento_neto_cetes_anual - inflacion
    
    # Utilidades Totales
    utilidad_bruta = monto_cetes + interes_bruto_cetes
    principal = utilidad_bruta - isr_cetes
    utilidad_neta = principal - monto_cetes
    
    # --- Cálculos para Venta Anticipada ---
    if venta_anticipada:
        precio_venta_cetes = VN_CETES * (1 - (tdd_actual / 360) * dias_restantes)
        ganancia_venta_cetes = precio_venta_cetes - precio_cetes
        interes_bruto_cetes_anticipado = titulos_cetes * ganancia_venta_cetes
        isr_cetes_anticipado = interes_bruto_cetes_anticipado * (isr_percent / 100.0)
        interes_neto_cetes_anticipado = interes_bruto_cetes_anticipado - isr_cetes_anticipado
        
        tasa_rendimiento_venta_periodo = (ganancia_venta_cetes / precio_cetes) * 100
        tasa_rendimiento_neta_periodo = tasa_rendimiento_venta_periodo - (isr_percent / 100.0)
        tasa_rendimiento_real_periodo = tasa_rendimiento_neta_periodo - inflacion
        
        tasa_rendimiento_venta = (ganancia_venta_cetes * 360 / (precio_cetes * dias_transcurridos)) * 100
        tasa_rendimiento_neta = tasa_rendimiento_venta - (isr_percent / 100.0)
        tasa_rendimiento_real = tasa_rendimiento_neta - inflacion
        
        utilidad_bruta_anticipado = monto_cetes + interes_bruto_cetes_anticipado
        principal_anticipado = utilidad_bruta_anticipado - isr_cetes_anticipado
        utilidad_neta_anticipado = principal_anticipado - monto_cetes
    
    # --- MOSTRAR RESULTADOS ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Venta al Vencimiento")
        st.metric("Capital Disponible", f"${monto_cetes:,.0f} MXN", help="Monto total destinado a la inversión en CETES.")
        st.metric("Precio de Compra", f"${precio_cetes:,.8f} MXN", help="Precio calculado con la tasa de descuento original.")
        st.metric("Capital Invertido", f"${inversion_cetes:,.2f} MXN", help="Monto utilizado en la compra de CETES.")
        st.metric("Títulos Comprados", f"{titulos_cetes:,d}", help="Cantidad de títulos adquiridos (títulos enteros).")
        st.metric("Remanente", f"${remanente_cetes:,.2f} MXN", help="Capital no invertido en títulos.")
    
        st.markdown("**Rendimientos Anualizados:**")
        st.metric("Rendimiento Nominal", f"{rendimiento_nominal_cetes_anual:.8f}%", help="Rendimiento anualizado sin aplicar ISR.")
        st.metric("Rendimiento Neto", f"{rendimiento_neto_cetes_anual:.8f}%", help="Rendimiento anualizado después de ISR.")
        st.metric("Rendimiento Real", f"{rendimiento_real_cetes_anual:.8f}%", help="Rendimiento anualizado ajustado por ISR e inflación.")
    
        st.markdown("**Rendimientos del Periodo:**")
        st.metric("Rendimiento Nominal", f"{rendimiento_nominal_cetes:.8f}%", help="Rendimiento obtenido durante el periodo sin impuestos.")
        st.metric("Rendimiento Neto", f"{rendimiento_neto_cetes:.8f}%", help="Rendimiento obtenido durante el periodo después de ISR.")
        st.metric("Rendimiento Real", f"{rendimiento_real_cetes:.8f}%", help="Rendimiento obtenido durante el periodo ajustado por inflación.")
    
        st.markdown("**Interés y Utilidad:**")
        st.metric("Interés Bruto", f"${interes_bruto_cetes:,.2f} MXN", help="Ganancia total sin ISR.")
        st.metric("ISR", f"${isr_cetes:,.2f} MXN", help="Impuesto aplicado al interés bruto.")
        st.metric("Interés Neto", f"${interes_neto_cetes:,.2f} MXN", help="Ganancia después de ISR.")
        st.metric("Utilidad Bruta", f"${utilidad_bruta:,.8f} MXN", help="Suma del capital invertido y el interés bruto.")
        st.metric("Utilidad Real (Principal)", f"${principal:,.8f} MXN", help="Utilidad bruta menos ISR y el capital invertido.")
    
    with col2:
        if venta_anticipada:
            st.markdown("#### Venta Anticipada")
            st.metric("Capital Disponible", f"${monto_cetes:,.0f} MXN", help="Monto destinado a la inversión.")
            st.metric("Precio de Compra", f"${precio_cetes:,.8f} MXN", help="Precio de compra con la tasa original.")
            st.metric("Capital Invertido", f"${inversion_cetes:,.2f} MXN", help="Monto invertido en CETES.")
            st.metric("Títulos Comprados", f"{titulos_cetes:,d}", help="Número de títulos adquiridos.")
            st.metric("Remanente", f"${remanente_cetes:,.2f} MXN", help="Capital no invertido en títulos.")
    
            st.markdown("**Rendimientos Anualizados (Venta Anticipada):**")
            st.metric("Rendimiento Nominal", f"{tasa_rendimiento_venta:.8f}%", help="Rendimiento anualizado sin ISR ni inflación.")
            st.metric("Rendimiento Neto", f"{tasa_rendimiento_neta:.8f}%", help="Rendimiento anualizado después de ISR.")
            st.metric("Rendimiento Real", f"{tasa_rendimiento_real:.8f}%", help="Rendimiento anualizado ajustado por ISR e inflación.")
    
            st.markdown("**Rendimientos del Periodo (Venta Anticipada):**")
            st.metric("Rendimiento Nominal", f"{tasa_rendimiento_venta_periodo:.8f}%", help="Rendimiento del periodo sin ISR.")
            st.metric("Rendimiento Neto", f"{tasa_rendimiento_neta_periodo:.8f}%", help="Rendimiento del periodo después de ISR.")
            st.metric("Rendimiento Real", f"{tasa_rendimiento_real_periodo:.8f}%", help="Rendimiento del periodo ajustado por inflación.")
    
            st.markdown("**Interés y Utilidad (Venta Anticipada):**")
            st.metric("Interés Bruto", f"${interes_bruto_cetes_anticipado:,.2f} MXN", help="Ganancia total en venta anticipada sin ISR.")
            st.metric("ISR", f"${isr_cetes_anticipado:,.2f} MXN", help="Impuesto aplicado en venta anticipada.")
            st.metric("Interés Neto", f"${interes_neto_cetes_anticipado:,.2f} MXN", help="Ganancia en venta anticipada después de ISR.")
            st.metric("Utilidad Bruta", f"${utilidad_bruta_anticipado:,.8f} MXN", help="Capital invertido más el interés bruto en venta anticipada.")
            st.metric("Utilidad Real (Principal)", f"${principal_anticipado:,.8f} MXN", help="Utilidad bruta menos ISR y el capital invertido en venta anticipada.")
        else:
            st.info("Activa la opción de **'Venta Anticipada'** para ver estos resultados. 🤓")
    
    with col3:
        if venta_anticipada:
            st.markdown("#### Ajuste por Venta Anticipada")
            st.metric("Precio de Compra (Tasa Original)", f"${precio_cetes:,.8f} MXN", help="Precio calculado con la tasa de descuento original.")
            st.metric("Precio de Venta (Tasa Actual)", f"${precio_venta_cetes:,.8f} MXN", help="Precio calculado con la tasa de descuento actual.")
            st.metric("Ganancia por Venta", f"${ganancia_venta_cetes:,.8f} MXN", help="Diferencia entre el precio de venta y el de compra.")
    
    st.markdown("---")
    st.header("Exportar Resultados 📄")
    # Crear diccionario con los principales resultados a exportar
    resultados_dict = {
        "CETES": "Simulación",
        "Monto Invertido": f"${monto_cetes:,.8f}",
        "Plazo": f"{dias} días",
        "Tasa de Desc. Original": f"{tdd_percent}%",
        "ISR": f"{isr_percent}%",
        "Inflación": f"{inflacion}%",
        "Precio de Compra": f"${precio_cetes:,.8f}",
        "Títulos Comprados": f"{titulos_cetes:,d}",
        "Remanente": f"${remanente_cetes:,.8f}",
        "Rend. Nominal (Anual)": f"{rendimiento_nominal_cetes_anual:.8f}%",
        "Rend. Neto (Anual)": f"{rendimiento_neto_cetes_anual:.8f}%",
        "Rend. Real (Anual)": f"{rendimiento_real_cetes_anual:.8f}%",
        "Rend. Nominal (Periodo)": f"{rendimiento_nominal_cetes:.8f}%",
        "Rend. Neto (Periodo)": f"{rendimiento_neto_cetes:.8f}%",
        "Rend. Real (Periodo)": f"{rendimiento_real_cetes:.8f}%",
        "Interés Bruto": f"${interes_bruto_cetes:,.8f}",
        "ISR (Interés)": f"${isr_cetes:,.8f}",
        "Interés Neto": f"${interes_neto_cetes:,.8f}",
        "Utilidad Bruta": f"${utilidad_bruta:,.8f}",
        "Utilidad Real": f"${principal:,.8f}",
    }
    
    pdf_bytes = generar_pdf(resultados_dict)
    st.download_button(
        label="Descargar PDF con Resultados 📥",
        data=pdf_bytes,
        file_name="simulacion_inversion.pdf",
        mime="application/pdf"
    )

# ================================
# Pie de Página
# ================================
st.markdown("---")
st.markdown("""
🎓 **SEMINARIO DE INVERSIÓN Y MERCADOS FINANCIEROS - IPN**  
🧑💻 Realizado por **J. Cruz Gómez** • 📧 josluigomez@gmail.com  
🔮 *"Los datos son como el acero: en bruto no valen, procesados son invencibles"*
""")
