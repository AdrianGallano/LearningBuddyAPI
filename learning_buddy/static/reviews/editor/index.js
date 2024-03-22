const editor = document.getElementById('editor')
const options = {
    debug: 'info',
    modules: {
        toolbar: true
    },
    theme: 'snow'
}

const quill = new Quill(editor, options)

const toolbar = document.querySelector('[role="toolbar"]')
// toolbar.classList.add("dark:bg-gray-50")