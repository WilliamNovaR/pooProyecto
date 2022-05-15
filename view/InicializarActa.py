from model.EvalEstudiante import EvaluacionEstudiante
from datetime import datetime

#inicializa la acta
def agregar_datos(st, controller):
    mes = int(datetime.today().strftime('%m')) #optiene el mes para saber en que semestre estamos
    st.title("Calificar Trabajos")
    evaluacion_obj = EvaluacionEstudiante()
    evaluacion_obj.id_estudiante = st.text_input("Id estudiante")
    #si el mes es inferior a 7 toma como si fuera el semestre 1 en otro caso lo toma como semestre 2 esto es importante para la acta
    if mes < 7:
        evaluacion_obj.periodo = datetime.today().strftime('%Y') + '-' + '1: '
    else:
        evaluacion_obj.periodo = datetime.today().strftime('%Y') + '-' + '2: '
    #lee datos de inicializacion de acta
    evaluacion_obj.periodo = st.text_input("Periodo de evaluacion", value=evaluacion_obj.periodo)
    evaluacion_obj.nombre_autor = st.text_input("Nombre del autor")
    evaluacion_obj.tipo_trabajo = st.radio("Tipo de trabajo", ('Aplicado', 'Investigacion'))
    evaluacion_obj.nombre_trabajo = st.text_input("Nombre del trabajo")
    evaluacion_obj.nombre_director = st.text_input("Nombre del director")
    st.write("El trabajo tiene codirector?")
    coodirector = st.radio("El trabajo tiene codirector?", ('Si', 'No'))
    if coodirector == 'Si':#pregunta si tiene codirector para preguntar el nombre o no
        evaluacion_obj.nombre_codirector = st.text_input("Nombre del codirector")
    evaluacion_obj.enfasis = st.text_input("Enfasis en:")
    evaluacion_obj.nombre_jurado1 = st.text_input("Nombre del jurado1")
    evaluacion_obj.nombre_jurado2 = st.text_input("Nombre del jurado2")
    #pregunta el numero del acta desde el cual se va a empezar
    if len(controller.evaluaciones) > 0:
        evaluacion_obj.inicilizar = st.number_input("Numero de acta:", value=controller.evaluaciones[
                                                                                 len(controller.evaluaciones) - 1].inicilizar + 1,
                                                    step=1)#se sugiere el numero siguiente al de la anterior calificacion
    else:
        evaluacion_obj.inicilizar = st.number_input("Numero de acta:", step=1) #en caso de no haber calificaciones anteriores no se sugiere nada
    enviado_btn = st.button("Send")

    if enviado_btn:
        controller.agregar_evaluacion(evaluacion_obj)
        st.success("Evaluacion agregada exitosamente")
    else:
        st.error("Faltan criterios por calificar!")

    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller