import axios from 'axios';

export const testConnection = async () => {
	try {
		const response = await axios.get('http://127.0.0.1:5000/test');
		console.log(response.data);
	} catch (error) {
		console.error('Error connecting to backend:', error);
	}
};

export const getTopEmails = async () => {
	const response = await axios.get('http://127.0.0.1:5000/top-emails');

	return response.data.top_emails;
};