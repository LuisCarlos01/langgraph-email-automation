import { useState, useEffect } from 'react'
import axios from 'axios'

interface Email {
  id: string
  subject: string
  sender: string
  status: string
  created_at: string
}

export default function Dashboard() {
  const [emails, setEmails] = useState<Email[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchEmails = async () => {
      try {
        const response = await axios.get('/api/v1/email/history')
        setEmails(response.data)
      } catch (error) {
        console.error('Erro ao carregar emails:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchEmails()
  }, [])

  return (
    <div className="px-4 sm:px-6 lg:px-8">
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-base font-semibold leading-6 text-gray-900">
            Emails Recentes
          </h1>
          <p className="mt-2 text-sm text-gray-700">
            Lista de emails processados recentemente pelo sistema.
          </p>
        </div>
      </div>
      <div className="mt-8 flow-root">
        <div className="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
            {loading ? (
              <div className="text-center">Carregando...</div>
            ) : (
              <table className="min-w-full divide-y divide-gray-300">
                <thead>
                  <tr>
                    <th
                      scope="col"
                      className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0"
                    >
                      Assunto
                    </th>
                    <th
                      scope="col"
                      className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                    >
                      Remetente
                    </th>
                    <th
                      scope="col"
                      className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                    >
                      Status
                    </th>
                    <th
                      scope="col"
                      className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                    >
                      Data
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200">
                  {emails.map((email) => (
                    <tr key={email.id}>
                      <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0">
                        {email.subject}
                      </td>
                      <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                        {email.sender}
                      </td>
                      <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                        {email.status}
                      </td>
                      <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                        {new Date(email.created_at).toLocaleDateString()}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        </div>
      </div>
    </div>
  )
} 