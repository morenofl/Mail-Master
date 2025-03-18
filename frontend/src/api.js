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


export const fetchEmails = async () => {
	try {
		const response = await axios.get('http://localhost:5000/emails');
		return response.data;  // Assuming response is an array of emails
	} catch (error) {
		console.error('Error fetching emails:', error);
		return [];
	}
};