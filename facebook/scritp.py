import re

def remove_non_essential_scripts(file_path, output_path):
    """
    Elimina scripts no esenciales (externos o identificados como seguros de eliminar) de un archivo HTML.

    :param file_path: Ruta del archivo HTML a procesar.
    :param output_path: Ruta del archivo de salida.
    """
    try:
        # Leer el archivo original
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Identificar scripts externos con "src" y sin atributos críticos
        external_script_pattern = re.compile(r'<script\s+[^>]*src=["\'].*?["\'].*?>.*?</script>', re.DOTALL | re.IGNORECASE)
        
        # Eliminar únicamente los scripts externos
        cleaned_content = re.sub(external_script_pattern, '', content)
        
        # Opcional: Identificar y mantener ciertos scripts específicos
        # Por ejemplo, no eliminar si contiene 'essential' en el contenido
        inline_script_pattern = re.compile(r'<script(?!.*essential).*?>.*?</script>', re.DOTALL | re.IGNORECASE)
        cleaned_content = re.sub(inline_script_pattern, '', cleaned_content)
        
        # Escribir el contenido limpio en el archivo de salida
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(cleaned_content)
        
        print(f"Scripts no esenciales eliminados exitosamente. Archivo limpio guardado en: {output_path}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
file_path = "index-2.html"  # Reemplaza con la ruta de tu archivo HTML
output_path = "index.html"  # Reemplaza con la ruta del archivo de salida
remove_non_essential_scripts(file_path, output_path)
