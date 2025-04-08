<?php
session_start();
require 'db.php';

$email = $_POST['email'] ?? '';
$password = $_POST['password'] ?? '';

if (!$email || !$password) {
    echo json_encode(['success' => false, 'message' => 'Missing email or password.']);
    exit;
}

// Track attempts (optional: IP-based)
$stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$email]);
$user = $stmt->fetch();

if (!$user) {
    echo json_encode(['success' => false, 'message' => 'User not found.']);
    exit;
}

// Simulate account lock after 5 failed attempts
if ($user['failed_attempts'] >= 5) {
    echo json_encode(['success' => false, 'message' => 'Account locked due to multiple failed attempts.']);
    exit;
}

if (password_verify($password, $user['password'])) {
    // Reset attempts
    $pdo->prepare("UPDATE users SET failed_attempts = 0 WHERE email = ?")->execute([$email]);

    // Simulate sending 2FA code
    $_SESSION['pending_2fa'] = true;
    $_SESSION['email'] = $email;
    $_SESSION['2fa_code'] = '123456'; // replace with generated code

    echo json_encode(['success' => true, 'message' => '2FA required']);
} else {
    // Increment failed attempts
    $pdo->prepare("UPDATE users SET failed_attempts = failed_attempts + 1 WHERE email = ?")->execute([$email]);

    echo json_encode(['success' => false, 'message' => 'Incorrect password.']);
}
?>