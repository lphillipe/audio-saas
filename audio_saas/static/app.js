// Elementos do DOM
const dropZone = document.getElementById('dropZone');
const audioFileInput = document.getElementById('audioFile');
const uploadBtn = document.getElementById('uploadBtn');
const processingSection = document.getElementById('processingSection');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');

// Estado
let selectedFile = null;

// Clique na área de upload
dropZone.addEventListener('click', () => {
    audioFileInput.click();
});

// Seleção de arquivo via input
audioFileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        selectFile(e.target.files[0]);
    }
});

// Drag and drop
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    
    if (e.dataTransfer.files.length > 0) {
        selectFile(e.dataTransfer.files[0]);
    }
});

// Selecionar arquivo
function selectFile(file) {
    selectedFile = file;
    dropZone.querySelector('p').textContent = `✅ ${file.name}`;
    uploadBtn.disabled = false;
}

// Upload do arquivo
uploadBtn.addEventListener('click', async () => {
    if (!selectedFile) return;

    // Mostra seção de processamento
    document.querySelector('.upload-section').classList.add('hidden');
    processingSection.classList.remove('hidden');

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
        const response = await fetch('/audio/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Erro ao processar áudio');
        }

        const data = await response.json();
        showResults(data);

    } catch (error) {
        showError(error.message);
    }
});

// Mostrar resultados
function showResults(data) {
    processingSection.classList.add('hidden');
    resultsSection.classList.remove('hidden');

    // Preenche transcrição completa
    document.getElementById('fullTranscription').textContent = data.transcription;

    // Preenche resumos
    document.getElementById('summaryCurto').textContent = data.summaries.curto;
    document.getElementById('summaryMedio').textContent = data.summaries.medio;
    document.getElementById('summaryDetalhado').textContent = data.summaries.detalhado;
}

// Mostrar erro
function showError(message) {
    processingSection.classList.add('hidden');
    errorSection.classList.remove('hidden');
    document.getElementById('errorMessage').textContent = message;
}
