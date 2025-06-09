import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'
import NotFound from './pages/NotFound'

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      
      <Route path="/" element={<Layout />}>
        <Route index element={<Dashboard />} />
        {/* Adicione mais rotas aqui */}
      </Route>
      
      <Route path="*" element={<NotFound />} />
    </Routes>
  )
}

export default App 