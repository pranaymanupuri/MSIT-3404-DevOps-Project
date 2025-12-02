function refreshStatus() {
    const backendStatus = document.querySelector('#backend-status .status-indicator');
    const frontendStatus = document.querySelector('#frontend-status .status-indicator');
    
    // Simulate successful connection
    backendStatus.textContent = 'Running ✅';
    backendStatus.style.color = 'green';
    
    frontendStatus.textContent = 'Running ✅';
    frontendStatus.style.color = 'green';
}

document.addEventListener('DOMContentLoaded', refreshStatus);