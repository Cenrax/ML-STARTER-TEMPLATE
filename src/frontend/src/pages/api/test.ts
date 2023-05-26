import { NextApiRequest, NextApiResponse } from 'next'
import axios from 'axios'


const handler = async (
  req: NextApiRequest,
  res: NextApiResponse,
 
): Promise<void> => {

    try {
        const { key } = req.query;
        const apiUrl = `http://localhost:8000/get/${key}`;
    
        // Forward the request to the FastAPI server
        const response = await axios.get(apiUrl);
        const data = response.data;
    
        // Return the response from the FastAPI server
        res.status(response.status).json(data);
      } catch (error : any) {
        console.error(error);
        res.status(error.response?.status || 500).json({ message: 'Internal server error' });
      }
}

export default handler
