import './App.css'
import InputForm from './components/input_form/input_form.component'


function App() {
  return (
    <div className='main-container'>
      <div className='main-left-container'>
        <h1>California Home Price Predictor</h1>
        <p>Enter the details of the house to predict its price.</p>
        <InputForm />
      </div>
    </div>
  )
}

export default App
