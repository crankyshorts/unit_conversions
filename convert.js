document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('conversionForm');
    const conversionType = document.getElementById('conversionType');
    const fromUnit = document.getElementById('fromUnit');
    const toUnit = document.getElementById('toUnit');
    const resultContainer = document.getElementById('resultContainer');
    const resultValue = document.getElementById('resultValue');
    const errorContainer = document.getElementById('errorContainer');
    const errorMessage = document.getElementById('errorMessage');

    // Update available units when conversion type changes
    conversionType.addEventListener('change', function() {
        const selectedType = this.value;
        updateUnitOptions(fromUnit, selectedType);
        updateUnitOptions(toUnit, selectedType);
    });

    // Handle form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (!form.checkValidity()) {
            e.stopPropagation();
            form.classList.add('was-validated');
            return;
        }

        const formData = new FormData();
        formData.append('value', document.getElementById('inputValue').value);
        formData.append('from_unit', fromUnit.value);
        formData.append('to_unit', toUnit.value);

        // Show loading state
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Converting...';
        submitBtn.disabled = true;

        fetch('/convert', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showResult(data.result);
                hideError();
            } else {
                showError(data.error);
                hideResult();
            }
        })
        .catch(error => {
            showError('An error occurred during conversion');
            hideResult();
        })
        .finally(() => {
            // Restore button state
            submitBtn.innerHTML = originalBtnText;
            submitBtn.disabled = false;
        });
    });

    function updateUnitOptions(selectElement, selectedType) {
        const options = selectElement.querySelectorAll('option');
        options.forEach(option => {
            if (option.dataset.type === selectedType) {
                option.style.display = '';
            } else {
                option.style.display = 'none';
            }
        });
        // Select first visible option
        const firstVisibleOption = Array.from(options).find(option => option.style.display !== 'none');
        if (firstVisibleOption) {
            selectElement.value = firstVisibleOption.value;
        }
    }

    function showResult(value) {
        resultValue.textContent = `Result: ${value} ${toUnit.value}`;
        resultContainer.style.display = 'block';
        resultContainer.scrollIntoView({ behavior: 'smooth' });
    }

    function hideResult() {
        resultContainer.style.display = 'none';
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorContainer.style.display = 'block';
    }

    function hideError() {
        errorContainer.style.display = 'none';
    }

    // Initialize unit options
    updateUnitOptions(fromUnit, conversionType.value);
    updateUnitOptions(toUnit, conversionType.value);
});
