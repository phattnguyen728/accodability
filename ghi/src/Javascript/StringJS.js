import React, { useState, useEffect, useRef } from 'react';
import 'codemirror/lib/codemirror.css';
import 'codemirror/theme/material.css';
import 'codemirror/mode/javascript/javascript.js';
import CodeMirror from 'codemirror';

const StringJS = () => {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');

  const runCode = () => {
    try {
      // eslint-disable-next-line no-new-func
      const result = new Function(code)();
      if (result !== undefined) {
        setOutput(result.toString());
      } else {
        setOutput('Output is undefined');
      }
    } catch (error) {
      setOutput(`Error: ${error.message}`);
    }
  };

  const textareaRef = useRef(null);

  useEffect(() => {
    const codemirrorOptions = {
      lineNumbers: true,
      mode: 'javascript',
      theme: 'material',
    };

    const editor = CodeMirror.fromTextArea(textareaRef.current, codemirrorOptions);
    editor.on('change', () => {
      setCode(editor.getValue());
    });
  }, []);

  return (
    <div style={{ paddingLeft: '20px' }}>
      <h1>JavaScript Code Editor</h1>
      <textarea ref={textareaRef}></textarea>
      <button onClick={runCode}>Run Code</button>
      <div>
        <strong>Output:</strong>
        <pre>{output}</pre>
      </div>
      <div>
        <h2>JavaScript String Tutorial</h2>
        <p>
          A collection of characters (letters, numbers, symbols) is known as a
          string. Strings must begin and end with quotation marks. Either single
          ' or double " will work, so long as you use the same at the beginning
          and end.
        </p>
        <p>Example:</p>
        <pre>'Hello, World!'</pre>
      </div>
    </div>
  );
};

export default StringJS;
