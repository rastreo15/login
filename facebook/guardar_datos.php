<?php
// Configuración de la base de datos
$servidor = "localhost";
$usuario = "root"; // Cambia si tu usuario de base de datos es distinto
$password = "tu_contraseña"; // Cambia por la contraseña de tu base de datos
$base_datos = "formulario_db";

// Crear conexión
$conn = new mysqli($servidor, $usuario, $password, $base_datos);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtener datos del formulario
$email = $_POST['email'];
$password = $_POST['pass'];

// Validar que no estén vacíos
if (!empty($email) && !empty($password)) {
    // Encriptar contraseña
    $password_hash = password_hash($password, PASSWORD_BCRYPT);

    // Preparar e insertar en la base de datos
    $sql = "INSERT INTO usuarios (email, password_hash) VALUES (?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $email, $password_hash);

    if ($stmt->execute()) {
        echo "Datos guardados correctamente.";
    } else {
        echo "Error al guardar los datos: " . $conn->error;
    }

    $stmt->close();
} else {
    echo "Por favor, completa todos los campos.";
}

// Cerrar conexión
$conn->close();
?>
